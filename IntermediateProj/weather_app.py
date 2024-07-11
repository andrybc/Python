import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

#create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("600x600")

city_label = tk.Label(root, text="City: ")
city_label.pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack()

get_button = tk.Button(root, text="Retrieve Weather")
get_button.pack()

weather_icon = tk.Label(root, image=None)
weather_icon.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()



def get_weather():
    city = city_entry.get()
    apiKey = ""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=imperial"
    
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        
        icon = data["weather"][0]["icon"]
        icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
        icon_response = requests.get(icon_url)
        icon_data = icon_response.content
        icon_image = Image.open(io.BytesIO(icon_data))
        icon_photo = ImageTk.PhotoImage(icon_image)
        weather_icon.config(image=icon_photo)
        weather_icon.image = icon_photo
        
        
        weather_label.config(text=f"Temperature: {temp} F\n Weather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")
        

get_button.config(command=get_weather)

root.mainloop()
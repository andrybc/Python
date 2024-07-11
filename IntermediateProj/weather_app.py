import requests
import tkinter as tk
from tkinter import messagebox


#create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("600x600")

city_label = tk.Label(root, text="City: ")
city_label.pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack()

get_button = tk.Button(root, text="Retrieve Weather", command=get_weather)
get_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()



def get_weather():
    pass


root.mainloop()
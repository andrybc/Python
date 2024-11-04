import PySimpleGUI as sg


sg.change_look_and_feel('GreenTan')

layout = [
    [sg.Text("Enter distance in kilometers"), sg.Input(key = '-KILO', do_not_clear = False, size= (5,1))]

]


window = sg.Window( title = "FirstTest", layout = layout, margins = (300,300)).read()

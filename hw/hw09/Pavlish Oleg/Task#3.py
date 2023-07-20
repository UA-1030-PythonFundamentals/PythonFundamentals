import tkinter as tk
from tkinter import font
from pyowm import OWM
HEIGHT = 350
WIDTH = 450
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()
def get_weather():
    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather
    text = tk.Label(text=f'Status: {w.detailed_status}', fg="Black", font=("Helvetica", 12))
    text.place(x=70,y=120)
    text = tk.Label(text=f'Wind speed: {w.wind()["speed"]}', fg="Black", font=("Helvetica", 12))
    text.place(x=70,y=140)
    text = tk.Label(text=f'Humidity: {w.humidity}', fg="Black", font=("Helvetica", 12))
    text.place(x=70,y=160)
    text = tk.Label(text=f"Temp: {w.temperature('celsius')['temp']}", fg="Black", font=("Helvetica", 12))
    text.place(x=70,y=180)
    text = tk.Label(text=f'Rain: {w.rain}', fg="Black", font=("Helvetica", 12))
    text.place(x=70,y=200)
    text = tk.Label(text=f'Index of heat: {w.heat_index}', fg="Black", font=("Helvetica", 12))
    text.place(x=70,y=220)
    text = tk.Label(text=f'Clouds: {w.clouds}', fg="Black", font=("Helvetica", 12))
    text.place(x=70,y=240)


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()
import tkinter as tk
from tkinter import font
from pyowm import OWM

HEIGHT = 350
WIDTH = 450

def get_weather(city):
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()


    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place('London,GB')
    w = observation.weather
    # print(w.detailed_status)         # 'clouds'
    # print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    # print(w.humidity)                # 87
    # print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    # print(w.rain)                    # {}
    # print(w.heat_index)              # None
    # print(w.clouds)                  # 75
    # print(ss)
    # pass
    text = (f"Місто: {city}\n" \
           f"Погодні умови: {w.detailed_status}\n" \
           f"Температура: {round(w.temperature('celsius')['temp'], 2)} °C\n" \
           f"Швидкість вітру: {w.wind()['speed']} км/г\n" \
           f"Вологість повітря: {w.humidity}")
    label['text'] = text


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Погода")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

name_var=tk.StringVar()
name_var.set('ведіть місто')
entry_field = tk.Entry(frame, font=('Courier', 12), textvariable = name_var)
# entry_field.textvariable = 'London,GB'
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


button = tk.Button(frame,
                   text="Отримати погоду",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather(name_var.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

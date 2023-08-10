##Task 2.
##You need combine two programs OWM.py and Tk_OWM.py
##into one working program.-- HW09 July 19, 2023 ---


import tkinter as tk
from tkinter import font
from pyowm import OWM

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

def get_weather():
    '''Retrieves weather forecast from remote server
    on the given location
    '''
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    city = entry_field.get()

    observation = mgr.weather_at_place(city)
    w = observation.weather
#
##    print(w.detailed_status)         # 'clouds'
##    print(w.wind())                  # {'speed': 4.6, 'deg': 330}
##    print(w.humidity)                # 87
##    print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
##    print(w.rain)                    # {}
##    print(w.heat_index)              # None
##    print(w.clouds)                  # 75

    det_stat = w.detailed_status
    tmp_cel = w.temperature('celsius')["temp"]
    clouds = w.clouds
    rain = w.rain
    humid = w.humidity
    wind = w.wind()

    label2 = tk.Label(lower_frame, text="In general - "+str(det_stat), font=('Courier', 8))
    label2.pack(side="bottom")
    label3 = tk.Label(lower_frame, text=('''Average temperature(C) : '''  + str(tmp_cel)), font=('Courier', 8))
    label3.pack(side="bottom")
    label4 = tk.Label(lower_frame, text="Clouds(%) : "+str(clouds), font=('Courier', 8))
    label4.pack(side="bottom")
    label5 = tk.Label(lower_frame, text="Rain : "+str(rain), font=('Courier', 8))
    label5.pack(side="bottom")
    label6 = tk.Label(lower_frame, text=('''Wind (m/s) : \n'''+str(wind)), font=('Courier', 8 ))
    label6.pack(side="bottom")
    label6 = tk.Label(lower_frame, text=("Humidity(%) : "+str(humid)), font=('Courier', 8))
    label6.pack(side="bottom")


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command = lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label1 = tk.Label(lower_frame, text = "Weather forecast for today:",  font=('Courier', 14,"bold"))
label1.pack(side="top")


root.mainloop()
#VN

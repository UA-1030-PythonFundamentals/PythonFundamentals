import tkinter as tk

from pyowm import OWM


def main():
    def update_label():
        label['text'] = weather_response()

    def weather_response():
        try:
            owm = OWM(API_KEY)
            mgr = owm.weather_manager()

            # Get input city from user entry field
            input_city = entry_value.get()

            # Check if city was entered
            if not input_city:
                return "In which city are you \ninterested in the weather?"

            # Search for current weather in London (Great Britain) and get details
            observation = mgr.weather_at_place(input_city)
            w = observation.weather

            # w.detailed_status         # 'clouds'
            # w.wind()                  # {'speed': 4.6, 'deg': 330}
            # w.humidity                # 87
            # w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
            # w.rain                    # {}
            # w.heat_index              # None
            # w.clouds                  # 75

            return f"City: {input_city}\n" \
                   f"Conditions: {w.detailed_status}\n" \
                   f"Temperature is {round(w.temperature('celsius')['temp'], 2)} °C\n" \
                   f"Wind speed is {w.wind()['speed']} km/hours\n" \
                   f"Humidity of the air is {w.humidity}"

        except Exception as e:
            return f'Oops! There was a problem\nretrieving that information.\n{e}'

    root = tk.Tk()
    canvas = tk.Canvas(root, height=350, width=450)
    root.title("Weather Application")
    canvas.pack()

    frame = tk.Frame(root, bg="deep sky blue", bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry_value = tk.StringVar()
    entry_field = tk.Entry(frame, textvariable=entry_value, font=('Courier', 12))
    entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

    button = tk.Button(frame,
                       text="Get Weather",
                       bg="gray", fg="white",
                       font=('Courier', 8),
                       command=lambda: update_label())
    button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    lower_frame = tk.Frame(root, bg='gold', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = tk.Label(lower_frame, font=('Courier', 14), anchor="w", justify="left")

    label.place(relx=0, rely=0, relwidth=1, relheight=1)

    root.mainloop()


if __name__ == '__main__':
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    main()

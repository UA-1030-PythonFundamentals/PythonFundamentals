# Калькулятор розбавлення спиртових розчинів

import tkinter as tk


def main():
    def update_label():
        result_label['text'] = mix_calculator()

    def mix_calculator():
        try:
            # Get spirit and drink strength from user entry fields
            spirit_st = float(spirit_strength.get())
            drink_st = float(drink_strength.get())

            # Check if strengths are valid
            if not 0 < drink_st < 100 or not 0 < spirit_st < 100:
                return "Це так не працює !!!\nМіцність має бути в діапазоні\nвід 0% до 100%"
            if drink_st > spirit_st:
                return "Це так не працює !!!\nМіцність напою має бути \nменша, ніж спирту"


            # Main calculations
            spirit_volume = round(drink_st / spirit_st * 1000)
            water_volume = round(1000 - spirit_volume)

            return f"Щоб отримати 1л бажаного напою\n" \
                   f"треба змішати: \n" \
                   f"{spirit_volume} мл спирту із\n" \
                   f"{water_volume} мл води."

        except Exception as e:
            return f'Виникла наступна помилка:\n{e}'

    root = tk.Tk()
    canvas = tk.Canvas(root, height=280, width=450)
    root.title("Калькулятор бутлегера")
    canvas.pack()

    # spirit frame
    spirit_frame = tk.Frame(root, bg="light blue", bd=5)
    spirit_frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.15, anchor='n')

    spirit_label = tk.Label(spirit_frame, text='Міцність вашого спирту, %: ', font=('Courier', 11, 'bold'))
    spirit_label.place(relx=0, rely=0, relwidth=0.8, relheight=1)

    spirit_strength = tk.StringVar()
    spirit_strength.set(96)

    spirit_field = tk.Entry(spirit_frame, textvariable=spirit_strength, font=('Courier', 12))
    spirit_field.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

    # drink frame
    drink_frame = tk.Frame(root, bg="light green", bd=5)
    drink_frame.place(relx=0.5, rely=0.23, relwidth=0.75, relheight=0.15, anchor='n')

    drink_label = tk.Label(drink_frame, text='Бажана міцність напою, %: ', font=('Courier', 11, 'bold'))
    drink_label.place(relx=0, rely=0, relwidth=0.8, relheight=1)

    drink_strength = tk.StringVar()
    drink_strength.set(40)

    drink_field = tk.Entry(drink_frame, textvariable=drink_strength, font=('Courier', 12))
    drink_field.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

    # button frame
    btn_frame = tk.Frame(root, bd=5)
    btn_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.15, anchor='n')

    button = tk.Button(btn_frame,
                       text="Розрахувати",
                       bg="green", fg="white",
                       font=('Courier', 11, 'bold'),
                       command=lambda: update_label())
    button.place(relx=0.25, rely=0, relwidth=0.5, relheight=1)

    # result frame
    result_frame = tk.Frame(root, bg='gold', bd=5)
    result_frame.place(relx=0.5, rely=0.57, relwidth=0.75, relheight=0.36, anchor='n')

    result_label = tk.Label(result_frame, font=('Courier', 12, 'bold'), anchor="w", justify="left")
    result_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    root.mainloop()


if __name__ == '__main__':
    main()

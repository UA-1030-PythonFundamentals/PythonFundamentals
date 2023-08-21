import tkinter as tk
from tkinter import *
import random

root = tk.Tk()
root.title("Злата і котики")
root.geometry("880x810")
root.resizable(False, False)


image_path1 = "mumb.png"
image_path2 = "Screen3.png"
image_path3 = "pinki1.png"


icon = PhotoImage(file = image_path1) 
root.iconphoto(False, icon)

bg = PhotoImage(file = image_path2)
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

logo = PhotoImage(file = image_path3)
logo1 = Label(image=logo)
logo1.place(x = 680, y = 450)


frame_plus = tk.Frame(root, bg="orange", bd=2)
frame_plus.place(x=240, y=10)
label_plus = Label(frame_plus, text="Додавання, натисни 'Далі ==>', щоб розпочати", fg="yellow", bg="salmon", font="Times 16")
label_plus.pack()

frame_minus = tk.Frame(root, bg="orange", bd=2)
frame_minus.place(x=240, y=160)
label_minus = Label(frame_minus, text="Віднімання, натисни 'Далі ==>', щоб розпочати", fg="yellow", bg="salmon", font="Times 16")
label_minus.pack()

frame_mno = tk.Frame(root, bg="orange", bd=2)
frame_mno.place(x=240, y=310)
label_mno = Label(frame_mno, text="Множення, натисни 'Далі ==>', щоб розпочати", fg="yellow", bg="salmon", font="Times 16")
label_mno.pack()

frame_tcount = tk.Frame(root, bg="orange", bd=5)
frame_tcount.place(x=95, y=450)
label_tcount = Label(frame_tcount, text="Результати відповідей:", fg="yellow", bg="salmon", font="Times 16")
label_tcount.pack()

frame_count = tk.Frame(root, bg="orange", bd=5)
frame_count.place(x=320, y=450)
label_count = Label(frame_count, fg="yellow", bg="salmon", font="Times 16")
label_count.pack()


count = 0

#1: a+b
def ab1_1():
    label_f4["text"] = ab1()


def ab1():

    tr = a + b
    r1 = int(entry2.get())
    
    if r1 == tr:
        return "ВІРНО"
    else:
        return "НЕ ВІРНО"


def rand1():
    global a, b, count
    
    if label_f4["text"] == "ВІРНО":
        count += 1
    elif label_f4["text"] == "НЕ ВІРНО":
        count -= 1   

    label_count["text"] = count
    entry2.delete(0, END)
    entry7.delete(0, END)
    entry12.delete(0, END)
    label_f4["text"] = ""
    label_f6["text"] = "(^_^)"
    label_f9["text"] = ""
    label_f11["text"] = "(^_^)"
    label_f14["text"] = ""
        
    a = random.randint(10, 100)
    b = random.randint(10, 100)
   
    label_f1["text"] = f"{a} + {b} = "
          

frame1 = tk.Frame(root, bg="deep sky blue", bd=5)
frame1.place(x=95, y=50)
label_f1 = Label(frame1, text="(^_^)", fg="white", bg="hotpink3", font="Times 22")
label_f1.pack()


frame2 = tk.Frame(root, bg="deep sky blue", bd=5)
frame2.place(x=240, y=50)
entry2 = tk.Entry(frame2, width=3, fg="white", bg="hotpink3", font="Times 23")
entry2.pack()

frame3 = tk.Frame(root, bg="deep sky blue", bd=5)
frame3.place(x=310, y=50)
button3 = tk.Button(frame3, text="Відповідь", bg="hotpink1", fg="white", font="Times 16", command=ab1_1)
button3.pack()

frame4 = tk.Frame(root, bg="deep sky blue", bd=5)
frame4.place(x=450, y=50)
label_f4 = Label(frame4, fg="white", bg="hotpink3", font = "Times 22")
label_f4.pack()

frame5 = tk.Frame(root, bg="light pink", bd=6)
frame5.place(x=610, y=50)
button5 = tk.Button(frame5, text="Далі ==>", bg="hotpink1", fg="white", font="Times 16", command=rand1)
button5.pack()

#2: a-b
def ab2_1():
    label_f9["text"] = ab2()

def ab2(): 

    if a > b:   
        tr = a - b
    else:
        tr = b - a

    r1 = int(entry7.get())
    
    if r1 == tr:
        return "ВІРНО"
    else:
        return "НЕ ВІРНО"





def rand2():
    global a, b, count

    if label_f9["text"] == "ВІРНО":
        count += 1
    elif label_f9["text"] == "НЕ ВІРНО":
        count -= 1   

    label_count["text"] = count
    entry2.delete(0, END)
    entry7.delete(0, END)
    entry12.delete(0, END)
    label_f1["text"] = "(^_^)"
    label_f4["text"] = ""
    label_f9["text"] = ""
    label_f11["text"] = "(^_^)"
    label_f14["text"] = ""

    a = random.randint(10, 100)
    b = random.randint(10, 100)
    
    if a > b:
        label_f6["text"] = f"{a} - {b} = "
    else:
        label_f6["text"] = f"{b} - {a} = "


frame6 = tk.Frame(root, bg="deep sky blue", bd=5)
frame6.place(x=95, y=200)
label_f6 = Label(frame6, text="(^_^)", fg="white", bg="hotpink3", font = "Times 22")
label_f6.pack()

frame7 = tk.Frame(root, bg="deep sky blue", bd=5)
frame7.place(x=240, y=200)
entry7 = tk.Entry(frame7, width= 3, fg="white", bg="hotpink3", font="Times 23")
entry7.pack()

frame8 = tk.Frame(root, bg="deep sky blue", bd=5)
frame8.place(x=310, y=200)
button8 = tk.Button(frame8, text="Відповідь", bg="hotpink1", fg="white", font="Times 16", command= ab2_1)
button8.pack()

frame9 = tk.Frame(root, bg="deep sky blue", bd=5)
frame9.place(x=450, y=200)
label_f9 = Label(frame9, fg="white", bg="hotpink3", font = "Times 22")
label_f9.pack()

frame10 = tk.Frame(root, bg="light pink", bd=6)
frame10.place(x=610, y=200)
button10 = tk.Button(frame10, text="Далі ==>", bg="hotpink1", fg="white", font="Times 16", command=rand2)
button10.pack()


#3: a*b
def ab3_1():
    label_f14["text"] = ab3()

def ab3():

    tr = a * b
    r1 = int(entry12.get())

    if r1 == tr:
        return "ВІРНО"
    else:
        return "НЕ ВІРНО"


def rand3():
    global a, b, count

    if label_f14["text"] == "ВІРНО":
        count += 1
    elif label_f14["text"] == "НЕ ВІРНО":
        count -= 1  

    label_count["text"] = count
    entry2.delete(0, END)
    entry7.delete(0, END)
    entry12.delete(0, END)
    label_f1["text"] = "(^_^)"
    label_f4["text"] = ""
    label_f6["text"] = "(^_^)"
    label_f9["text"] = ""
    label_f14["text"] = ""
       
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    
    label_f11["text"] = f"{a} * {b} = "


frame11 = tk.Frame(root, bg="deep sky blue", bd=5)
frame11.place(x=95, y=350)
label_f11 = Label(frame11, text="(^_^)", fg="white", bg="hotpink3", font = "Times 22")
label_f11.pack()

frame12 = tk.Frame(root, bg="deep sky blue", bd=5)
frame12.place(x=240, y=350)
entry12 = tk.Entry(frame12, width= 3, fg="white", bg="hotpink3", font="Times 23")
entry12.pack()

frame13 = tk.Frame(root, bg="deep sky blue", bd=5)
frame13.place(x=310, y=350)
button13 = tk.Button(frame13, text="Відповідь", bg="hotpink1", fg="white", font="Times 16", command=ab3_1)
button13.pack()

frame14 = tk.Frame(root, bg="deep sky blue", bd=5)
frame14.place(x=450, y=350)
label_f14 = Label(frame14, fg="white", bg="hotpink3", font="Times 22")
label_f14.pack()

frame15 = tk.Frame(root, bg="light pink", bd=6)
frame15.place(x=610, y=350)
button15 = tk.Button(frame15, text="Далі ==>", bg="hotpink1", fg="white", font="Times 16", command=rand3)
button15.pack()



root.mainloop()






#https://pythonassets.com/posts/drop-down-list-combobox-in-tk-tkinter/
import tkinter as tk
from tkinter import font
from tkinter import ttk,messagebox
from tkinter import *
from zodiac import zod


HEIGHT = 350
WIDTH = 450

window= tk.Tk()

################################--Elements of main window--####################################
window.title("---Твій знак Зодіаку---")
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH,bg="light blue")
canvas.pack()
################################==Used data arrays==##############################################
dlist = ['1', "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
       "13","14","15","16","17","18","19","20","21","22","23", '24',
       "25", '26', "27", "28", "29", "30", "31"]

mlist = ["Січень", "Лютий", "Березень", "Квітень",
            "Травень","Червень","Липень","Серпень",
            "Вересень","Жовтень","Листопад","Грудень"]

znak =["Овен", "Телець","Близнюки", "Рак", "Лев", "Діва", "Терези",
       "Скорпіон", "Змієносець", "Стрілець", "Козоріг", "Водолій","Риби"]

mes ="Твій зоряний знак : \n"
pom ="   Будь-ласка, \n введіть \n правильну дату ... "
################################################################################
selection1 = StringVar(window)
selection2 = StringVar(window)


selection1 = "Січень"
selection2 = 1
def selection_changed(event):
    '''ComboBox choice'''

    global selection1
    selection1 = combo1.get()
    #print("Місяць :",selection1)

def selection_changed2(event):
    '''ComboBox choice'''

    global selection2
    selection2 = int(combo2.get())
    #print("День :",selection2)

#############################################################################
def get_sign():
    '''Inquiry for the sign'''

    w = zod(selection1,selection2)
    if w in znak:
        myLabel = tk.Label(lower_frame1, text=f"{mes}\n{w}", bg='gold', font=('Courier', 11, 'bold'))
        myLabel.place(x=20,y=13)#.pack(side=LEFT)
    else:
        myLabel = tk.Label(lower_frame1, text=f"{pom}", bg='gold', font=('Courier', 11, 'bold'))#.pack(side=LEFT)
        myLabel.place(x=24, y=13)

###############################################################################################
frame1 = tk.Frame(window, bg="deep sky blue", bd=5)
frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

frame2 = tk.Frame(window, bg="deep sky blue", bd=5)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')

##############################== Поле Виводу Знаку==#################################################################
lower_frame1 = tk.Frame(window,  bg='gold', bd=10)
lower_frame1.place(relx=0.5, rely=0.65, relwidth=0.75, relheight=0.26, anchor='n')
##############################################################################################
label1 = tk.Label(frame1, text='Виберіть місяць народження:', font=('Courier', 11, 'bold'),bg="deep sky blue")
label1.pack(side=LEFT)#place(relx=0, rely=0, relwidth=0.8, relheight=1)

label2 = tk.Label(frame2, text='Виберіть дату народження:', font=('Courier', 11, 'bold'),bg="deep sky blue")
label2.pack(side=LEFT)#place(relx=0, rely=0, relwidth=0.8, relheight=1)
###############################################################################################
button = tk.Button(lower_frame1,
                   text="Клікни\n"+"щоб\n"+ "дізнатись",
                   bg="gray", fg="white",
                   font=('Courier', 10),
                   command = lambda: get_sign())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)
###################################--Drop-off menus--######################################
combo1 = ttk.Combobox(frame1,state="readonly",width = 10,
    values = mlist)
combo1.place(x=245, y=2)
combo1.set("Січень")
combo1.bind("<<ComboboxSelected>>", selection_changed)


combo2 = ttk.Combobox(frame2,state="readonly",width = 10,
    values = dlist)
combo2.set("1")
combo2.place(x=245, y=2)
combo2.bind("<<ComboboxSelected>>", selection_changed2)
######################
window.mainloop()

#--August 29 2023---VN

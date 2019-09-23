import tkinter as tk
from tkinter import *

window = Tk()

window.title("KGCE BE-IT 2020")
window.configure(background='black')
window.geometry('1280x680')


lbl = tk.Label(window, text="CHATBOT", width=60, fg="black", bg="white", height=2, font=('times', 24, ' bold'))
lbl.place(x=100, y=20)

frame = Frame(window)
frame.place(x=100, y=120, width=625, height=400)

sc = Scrollbar(frame)
msg = Listbox(frame, width=100, height=20)
sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH)

txt = tk.Entry(window, width=62, bg="white", fg="black", font=('times', 15, ' bold '))
txt.place(x=100, y=525)

btn = tk.Button(window, text="Send Message", fg="black", bg="white", width=20, height=1, activebackground = "Green", font=('times', 15, ' bold '))
btn.place(x=150, y=560)

btn1 = tk.Button(window, text="Clear Message", fg="black", bg="white", width=20, height=1, activebackground = "Red", font=('times', 15, ' bold '))
btn1.place(x=450, y=560)



lbl11 = tk.Label(window, text="Frequent Ask Question",  fg="red", bg="black", font=('times', 30, ' bold')) 
lbl11.place(x=800, y=120)

btn11 = tk.Button(window, text="What is your name ?", fg="black", bg="white", width=25, height=1, activebackground = "yellow", font=('times', 20, ' bold '))
btn11.place(x=800, y=200)

btn12 = tk.Button(window, text="How are you ?", fg="black", bg="white", width=25, height=1, activebackground = "yellow", font=('times', 20, ' bold '))
btn12.place(x=800, y=280)

btn13 = tk.Button(window, text="In which language you talk ?", fg="black", bg="white", width=25, height=1, activebackground = "yellow", font=('times', 20, ' bold '))
btn13.place(x=800, y=360)

btn14 = tk.Button(window, text="In which city you live ?", fg="black", bg="white", width=25, height=1, activebackground = "yellow", font=('times', 20, ' bold '))
btn14.place(x=800, y=440)

btn15 = tk.Button(window, text="Whats your upcoming plan ?", fg="black", bg="white", width=25, height=1, activebackground = "yellow", font=('times', 20, ' bold '))
btn15.place(x=800, y=520)



lbl21 = tk.Label(window, text="CHATBOT MINI-PROJECT BY KGCE BE-IT BATCH 2020, GROUP NO : 10", width=80, fg="white", bg="black", font=('times', 15, ' bold')) 
lbl21.place(x=200, y=620)

window.mainloop()

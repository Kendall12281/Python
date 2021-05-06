import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title("Calculator")

#Functions

def click(caracter):
	global text
	text = text + str(caracter)
	print_text.set(text)

def delete():
	global text
	text = ""
	print_text.set(text)

def operations():
	global text
	text = str(eval(text))
	print_text.set(text)
	text = ""

text = ""
print_text = StringVar()



#Entry
entry = Entry(root,bg="white", font =("Algerian", 10), textvariable=print_text).grid(row=1, column=1, columnspan=6, ipady=10, sticky="W E")



#Numbers
numero1 = Button(root, bg="#1B998B", text="1", font=('arial', 18, 'bold'), fg="black", cursor="hand2", command= lambda: click(1))
numero1.grid(row=2,column=1)

numero2 = Button(root, bg="#1B998B", text="2", font=('arial', 18, 'bold'), fg="black", cursor="hand2", command= lambda: click(2))
numero2.grid(row=2,column=2)

numero3 = Button(root, bg="#1B998B", text="3", font=('arial', 18, 'bold'), fg="black", cursor="hand2", command= lambda: click(3))
numero3.grid(row=2,column=3)

numero4 = Button(root, bg="#1B998B", text="4", font=('arial', 18, 'bold'), fg="black", cursor="hand2", command= lambda: click(4))
numero4.grid(row=2,column=4)

numero5 = Button(root, bg="#1B998B", text="5", font=('arial', 18, 'bold'), fg="black", cursor="hand2", command= lambda: click(5))
numero5.grid(row=2,column=5)

numero6 = Button(root, bg="#1B998B", text="6", font=('arial', 18, 'bold'), fg="black", cursor="hand2", command= lambda: click(6))
numero6.grid(row=3,column=1)

numero7 = Button(root, bg="#1B998B", text="7", font=('arial', 18, 'bold'), fg="black", cursor="hand2", command= lambda: click(7))
numero7.grid(row=3,column=2)

numero8 = Button(root, bg="#1B998B", text="8", font=('arial', 18, 'bold'), fg="black", cursor="hand2", command= lambda: click(8))
numero8.grid(row=3,column=3)

numero9 = Button(root, bg="#1B998B", text="9", font=('arial', 18, 'bold'), fg="black", cursor="hand2", command= lambda: click(9))
numero9.grid(row=3,column=4)

numero0 = Button(root, bg="#1B998B", text="0", font=('arial', 18, 'bold'), fg="black", cursor="hand2", command= lambda: click(0))
numero0.grid(row=3,column=5)

#Buttoms-others
delete2 = Button(root, bg="#BFD7EA", text="D\nE\nL\nE\nT\nE", height=6, widt=3, font=('arial', 10, 'bold'), fg="black", cursor="hand2", command= lambda: delete())
delete2.grid(row=2, rowspan=2, column=6)

multiply = Button(root, bg="#BFD7EA", text="X",width=8, font=('arial', 10, 'bold'), fg="black",  cursor="hand2", command= lambda: click("*"))
multiply.grid(row=4,columnspan=3)

divide = Button(root, bg="#BFD7EA", text="/",width=8, font=('arial', 10, 'bold'), fg="black",  cursor="hand2", command= lambda: click("/"))
divide.grid(row=4,column=3,columnspan=2)

rest = Button(root, bg="#BFD7EA", text="-",width=8, font=('arial', 10, 'bold'), fg="black", cursor="hand2", command= lambda: click("-"))
rest.grid(row=4,column=5, columnspan=3)

sumar = Button(root, bg="#BFD7EA", text="SUMAR",width=13, font=('arial', 10, 'bold'), fg="black",  cursor="hand2", command= lambda: click("+"))
sumar.grid(row=5, column=1, columnspan=3)

equal = Button(root, bg="#BFD7EA", text="EQUAL",width=13, font=('arial', 10, 'bold'), fg="black", cursor="hand2", command= lambda: operations())
equal.grid(row=5, column=4, columnspan=3)





root.mainloop()
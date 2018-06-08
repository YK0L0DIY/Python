#!/usr/bin/env python
import sys
sys.path.append("/usr/lib/tkinter")
from tkinter import *



window = Tk()
window.title("#converter")
window.config(background="black")

def click():
    text_entered=textentry.get()
    text_entered=text_entered.lower()
    n=len(text_entered)
    a=0
    k="#"
    while n!=a:
        alph="abcdefghijklmnopqrstuvxyzw"
        if text_entered[a]==" ":
            k=str(k)+str(" #")
            a+=1
        elif text_entered[a] in alph:
            k=str(k)+str(text_entered[a])
            a+=1
        else:
            a+=1
    text_out=k
    output.delete(0.0,END)
    output.insert(END,text_out)



Label (window, text="YOUR TEXT TO CONVERT:", bg="black" , fg="white").grid(row=0, column=0, sticky=W)

textentry = Entry(window,width=66, bg="white")
textentry.grid(row=1,column=0,sticky=W)

Button(window,text="CONVERT", width=63,command=click).grid(row=3,column=0,sticky=W)

Label (window,text="YOUR TEXT CONVERTED:",bg="black",fg="white").grid(row=5, column=0, sticky=W)

output= Text(window, width=75,height=6,wrap=WORD , background="white")
output.grid(row=6,column=0, sticky=W)



window.mainloop()

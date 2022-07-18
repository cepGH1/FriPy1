import tkinter as tk
from tkinter import BOTTOM, END, RAISED, RIGHT, Button, Toplevel, mainloop, ttk, BOTH, Frame, Canvas, PhotoImage, NW
from PIL import Image, ImageTk
from io import BytesIO as by
import requests as requests

root = tk.Tk()
root.geometry('600x600+30+30')
root.title('Main Window')
top1 = Toplevel()
top1.title('this is a child window')

top1.geometry('300x300+50+50')
realImage = Image.open('textPic1.jpg')
background_image=PhotoImage(file="12.png")
img = ImageTk.PhotoImage(realImage) 
canvas = Canvas(top1, width = 600, height = 600) 
canvas.pack(fill=BOTH, expand=1) 
canvas.create_image(20,20, anchor=NW, image=img)  
mainloop()

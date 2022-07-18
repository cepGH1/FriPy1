import tkinter as tk
from tkinter import BOTTOM, END, RAISED, RIGHT, Button, ttk, BOTH, Frame, Canvas, PhotoImage, NW
from PIL import Image, ImageTk
from io import BytesIO as by
import requests as requests

class MyTkWindow:
    def __init__(self, myAddress):
        print(myAddress)
        ims = requests.get(myAddress)
        realImage = Image.open(by(ims.content))
        root = tk.Tk()      
        canvas = Canvas(root, width = 600, height = 600)      
        canvas.pack()        
        img = ImageTk.PhotoImage(realImage)   
        canvas.create_image(20,20, anchor=NW, image=img)      
        root.mainloop()  




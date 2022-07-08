from gettext import gettext
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk



def findContent(url):
    URL = url
    r = requests.get(URL)
    #print(r.content)

    soup = BeautifulSoup(r.content, 'html5lib')

    myImages = soup.find_all("img")

    print(myImages)
    textM.set(str(myImages))
    T.insert(tk.END, textM.get() )
    

    


def loadUrl(s):
    URL2 = s
    print(URL2)

root = tk.Tk()
root.title("Menu Page")
#root.iconbitmap('./mic1.ico')
root.geometry('800x600+50+50')
textTitle = tk.StringVar()
textTitle.set("Enter url below")
myLabel = ttk.Label(root, textvariable=textTitle)
myLabel.pack()
textbox = ttk.Entry(root)
textbox.pack()
loadButton = ttk.Button(root, text="save URL", command=lambda : loadUrl(textbox.get()))
checkButton =  ttk.Button(root, text="press to extract image tags", command=lambda : findContent(textbox.get()))
textM = tk.StringVar()
textI = tk.StringVar()
textI.set("image tags will be displayed here")


msg = tk.Message(root, textvariable = textI)

loadButton.pack()

checkButton.pack()

T = tk.Text(root, height=8, width=70)
msg.pack()
T.pack()





root.mainloop()
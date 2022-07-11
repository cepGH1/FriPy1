from gettext import gettext
from turtle import right
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import BOTTOM, END, RIGHT, ttk
import mydb



def findContent(url):
    """finds all the image tags from a web page using beautiful soup"""
    URL = url
    r = requests.get(URL)
    #print(r.content)

    soup = BeautifulSoup(r.content, 'html5lib')

    myImages = soup.find_all("img")
    T.delete(1.0, END)

    print(myImages)
    for item in myImages:
        
        print(item['src'])
        textM.set(item['src'])
        T.insert(tk.END, textM.get() + "\n")
    sources =[]
    for var in range(len(myImages)):
        print(var)
            
def findContent2(num):
    T.delete(1.0, END) 
               

def addEntry(betterVar, test):
    mydb.addEntry(betterVar, test)

myWebAddresses = mydb.connectAndGetAllWebsites()
print(myWebAddresses[0]['address'])



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
notemessage = tk.StringVar()
notemessage.set("write notes here")
myNoteLabel = ttk.Label(root, textvariable=notemessage)
myNoteLabel.pack()
noteT = tk.Text(root, height=3, width=70)
noteT.pack()


checkButton =  ttk.Button(root, text="press to extract image tags", command=lambda : findContent(textbox.get()))
autoLoadButton = ttk.Button(root, text="load from database", command = lambda : findContent(myWebAddresses[0]['address']))
loadAddressButton = ttk.Button(root, text= "Add address to database", command = lambda : addEntry(textbox.get(), noteT.get('1.0','end')))
basesNumberLoadButton = ttk.Button(root, text="loads the address number from the database", command = lambda : findContent(myWebAddresses[int(textbox.get())]['address']))
textM = tk.StringVar()
textI = tk.StringVar()
textI.set("image tags will be displayed here")


msg = tk.Message(root, textvariable = textI)



checkButton.pack(side=RIGHT, padx=5, pady=5)
autoLoadButton.pack()
loadAddressButton.pack()
basesNumberLoadButton.pack()

T = tk.Text(root, height=8, width=70)
msg.pack()
T.pack()





root.mainloop()
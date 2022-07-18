import tkinter as tk
from tkinter import BOTTOM, END, RAISED, RIGHT, Button, Toplevel, ttk, BOTH, Frame, Canvas, NW

from matplotlib.pyplot import pause
import mydb
import requests
from bs4 import BeautifulSoup
import show_images1 as disp
import show_images2 as disp2
from PIL import Image, ImageTk
from io import BytesIO as by


sources =[]
anchors =[]
workingImages = []

def findContent(url):
    """finds all the image tags from a web page using beautiful soup"""
    URL = url
    r = requests.get(URL)
    #print(r.content)

    soup = BeautifulSoup(r.content, 'html5lib')

    myImages = soup.find_all("img")
    myLinks = soup.find_all("a")
    T.delete(1.0, END)
    K.delete(1.0, END)

    print(myImages)
    print(myLinks)
    sources.clear()
    
    if myImages:
        for item in myImages:
            print(item['src'])
            textM.set(item['src'])
            sources.append(item['src'])
            T.insert(tk.END, textM.get() + "\n")

    else:
        print("no images")

    if myLinks:
        for thing in myLinks:
            print(thing['href'])
            textK.set(thing['href'])
            anchors.append(thing['href']) 
            K.insert(tk.END, textK.get() + "\n")

    else:
        print("There are no anchors")

            
def findContent2(num):
    T.delete(1.0, END) 
               

def addEntry(betterVar, test):
    mydb.addEntry(betterVar, test)

def addFullEntry(address, images, notes):
    mydb.addFullEntry(address, images, notes)

def pressedButton1():
    pass

def getImages(myList):
    print(myList[0]) 
    workingImages.clear()        
    for item in myList:
        if "http" in item:
            try:
                ims = requests.get(item)
                realImage = Image.open(by(ims.content)) 
                realImage = realImage.resize((500,500))
            except:
                print("download failed")
                realImage = Image.open('FNF.jpg')

        elif item[0] != '.':
            fullAddress = textbox.get() + item
            try:
                ims = requests.get(fullAddress)
                realImage = Image.open(by(ims.content))
                realImage = realImage.resize((500,500))
            except:
                print("download failed")
                realImage = Image.open("FNF.jpg")
        else:
            realImage = Image.open('textPic1.jpg') 
        img = ImageTk.PhotoImage(realImage) 
        workingImages.append(img)
    

def showImages(myList):
    getImages(myList)
    for num in range(len(workingImages)):
        top2 = Toplevel(root) 
        top2.title("child") 
        myTop2Label = ttk.Label(top2, text="image number " + str(num)).pack()
        canvas = Canvas(top2, width = 600, height = 600) 
        canvas.pack()
        try:
            canvas.create_image(20,20, anchor=NW, image=workingImages[num])
            
        except:
            print("Image could not be loaded")

        
    
   
        
              
    
        
        
    
    


myWebAddresses = mydb.connectAndGetAllWebsites()
print(myWebAddresses[0]['address'])

root = tk.Tk()
root.title("This has frames")
root.geometry('800x800+30+30')
frame = Frame(root, relief=RAISED, borderwidth=1)
frame1 = Frame(root, relief=RAISED, borderwidth=1)
frame2 = Frame(root, relief=RAISED, borderwidth=1 )
frame3 = Frame(root, relief=RAISED, borderwidth=1)
textM = tk.StringVar()
textK = tk.StringVar()
textTitle = tk.StringVar()
textTitle.set("Enter url below")
myLabel = ttk.Label(frame, textvariable=textTitle)
myLabel.pack(padx=5, pady=5)
textbox = ttk.Entry(frame)
textbox.pack(padx=5, pady=5)
checkButton =  ttk.Button(frame, text="press to extract image tags", command=lambda : findContent(textbox.get()))
checkButton.pack(padx=5, pady=5)

textTitle2 = tk.StringVar()
textTitle2.set("Image relative addresses will be displayed here")
myLabel2 = ttk.Label(frame1, textvariable=textTitle2)
myLabel2.pack(padx=5, pady=5)
myTitle3 = tk.StringVar()
myTitle3.set("hrefs will be displayed here")
myLabel3 = ttk.Label(frame3, textvariable=myTitle3)
myLabel3.pack(padx=5, pady=5)
T = tk.Text(frame1, height=8, width=70)
T.pack(padx=5, pady=5)
K = tk.Text(frame3, height=8, width=70)
K.pack(padx=5, pady=5)
textTitle3 = tk.StringVar()
textTitle3.set("Enter notes about the url below")
myLabel3 = ttk.Label(frame2, textvariable=textTitle3)
myLabel3.pack(padx=5, pady=5)
myNotes = tk.Text(frame2, height=8, width=70)
myNotes.pack(padx=5, pady=5)
loadAddressButton = ttk.Button(frame2, text= "Add address and notes to database", command = lambda : addEntry(textbox.get(), myNotes.get('1.0','end')))
loadAddressButton.pack(padx=5, pady=5)


frame.pack(padx=5, pady=5)
frame2.pack(padx=5, pady=5)
frame1.pack(padx=5, pady=5)
frame3.pack(padx=5, pady=5)
button1 = Button(root, text="button1")
button1.pack(side=RIGHT, padx=5, pady=5)
button2 = Button(root, text="Save Full Entry", command = lambda : addFullEntry(textbox.get(), sources, myNotes.get('1.0', 'end')))
button2.pack(side=RIGHT, padx=5, pady=5)
button3 = Button(root, text="Show Images", command = lambda : showImages(sources) )
button3.pack(side=RIGHT, padx=5, pady=5)

root.mainloop()
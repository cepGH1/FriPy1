import requests as requests
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image
from io import BytesIO as by


print("show_images is imported")

class MyShower:

    def __init__(self, myImageAddress):
        ims = requests.get(myImageAddress)
        realImage = Image.open(by(ims.content))
        plt.title("Science")
        plt.xlabel("X pixel scaling")
        plt.ylabel("Y pixels scaling")
        #realImage = mpimg.imread('textPic1.jpg')
        plt.imshow(realImage)
        plt.show()



def Shower2(myArray):
    imageArray = myArray
    for item in imageArray:
        ims = requests.get(item)
        realImage = Image.open(by(ims.content))
        plt.title("Science")
        plt.xlabel("X pixel scaling")
        plt.ylabel("Y pixels scaling")
        #image = mpimg.imread()
        plt.imshow(realImage)
        plt.show()
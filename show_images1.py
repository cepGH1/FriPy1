import requests as requests
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image
from io import BytesIO

print("show_images is imported")


def Shower(images):
    imageArray = images
    

    for item in images:
        ims = requests.get(item)
        realImage = Image.open(BytesIO(ims.content))
        plt.title("Science")
        plt.xlabel("X pixel scaling")
        plt.ylabel("Y pixels scaling")
        #image = mpimg.imread()
        plt.imshow(realImage)
        plt.show()
       
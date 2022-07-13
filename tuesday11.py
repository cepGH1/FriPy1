import mydb
import requests
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image
from io import BytesIO

myWebbies = mydb.connectAndGetAllWebsites()
print(myWebbies)

print(myWebbies[8]['images'][0])

myPicAddress = myWebbies[8]['address'] + myWebbies[8]['images'][0]
print(myPicAddress)

ims = requests.get(myPicAddress)
#print(ims.content)
img = Image.open(BytesIO(ims.content))
plt.title("Science")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")


#image = mpimg.imread()
plt.imshow(img)
plt.show()









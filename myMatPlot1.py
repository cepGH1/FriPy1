from matplotlib import pyplot as plt
from matplotlib import image as mpimg
 
plt.title("carbonate")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")
 
image = mpimg.imread("12.png")
plt.imshow(image)
plt.show()
from bs4 import BeautifulSoup
import re
from urllib import request

# Define the remote file to retrieve
remote_url = 'http://www.cepfurchen.net/index.html'
# Define the local filename to save data
local_file = 'clare1.html'
# Download remote and save locally
request.urlretrieve(remote_url, local_file)


with open("alkynes.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
##creates a list of img full tags - 
alkyneImages = soup.find_all("img")
myWord = soup.find(text="Propyne")
#this is teh whole file
mySrc = soup.find_all(
)




for tag in soup.find_all(re.compile("im")):
    print(tag.name)


print(alkyneImages)
print(alkyneImages[0])
#print(myWord)
#print(mySrc)


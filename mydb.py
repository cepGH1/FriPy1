from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print("connected to localhost")

def connectAndGetAllWebsites():
    db = client.websites
    collection = db.websites
    myList = collection.find()
    myWebbies =[]
    for item in myList:
        print(item)
        myWebbies.append(item)

    client.close()
    return myWebbies



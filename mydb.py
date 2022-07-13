from pymongo import MongoClient


def connectAndGetAllWebsites():
    client = MongoClient('localhost', 27017)
    print("connected to localhost")
    db = client.websites
    collection = db.websites
    myList = collection.find()
    myWebbies =[]
    for item in myList:
        print(item)
        myWebbies.append(item)

    client.close()
    return myWebbies

def addEntry(address, notes):

    client = MongoClient('localhost', 27017)
    print("connected to localhost")
    db = client.websites
    collection = db.websites
    mydict = { "address": address, "images": "", "notes": notes }

    x = collection.insert_one(mydict)
    client.close()

def addFullEntry(address, images, notes):
    client = MongoClient('localhost', 27017)
    print("connected to localhost")
    db = client.websites
    collection = db.websites
    mydict = { "address": address, "images": images, "notes": notes }

    x = collection.insert_one(mydict)

    client.close()
    print("entry added")
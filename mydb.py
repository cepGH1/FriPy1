from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.movies
collection = db.movies
myList = collection.find()
for item in myList:
    print(item)

client.close()



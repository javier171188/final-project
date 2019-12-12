# import datetime module
import datetime
# import pymongo module
import pymongo
# connection string
client = pymongo.MongoClient("mongodb://uaqro:Croqueta1@cloud.mongodb.com/news")
# test
db = client['news']
# define collection
collection = db['news_clusters']
# sample data
document = {"company":"Capital One",
"city":"McLean",
"state":"VA",
"country":"US"}
# insert document into collection
id = collection.insert_one(document).inserted_id
print("id")
print(id)



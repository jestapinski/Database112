#Jordan Stapinski (jstapins) 15-112 Databse Techniques Tutorial
#Revised March 2017
#github.com/jestapinski/Database112

from pymongo import MongoClient
#Assumes you have a running Mongod instance on port 27017
client = MongoClient()

#Create any db you want on the fly
db = client.test_db

#Posting into db with table name tname
#tname created on the fly
post = {"name" : "Koz",
		"class" : "15-112"}
post_id = db.tname.insert_one(post).inserted_id
print(post_id)

for row in db.tname.find({"name": "Koz"}):
	print(row["name"], "Teaches", row["class"])
	#Do something with each returned row

#Change the course instructor
db.tname.update_one({"name":"Koz"}, {"$set" :{"name":"The TA's"}})
for row in db.tname.find():
	print(row["name"], "Teach", row["class"])

#And then you're fired :D
db.tname.delete_one({"name" : "The TA's"})
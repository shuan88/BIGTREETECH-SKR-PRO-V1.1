# pip install pymongo 
# pip install datetime   
import datetime
import pymongo


myclient = pymongo.MongoClient("mongodb://140.134.29.211:27017/")
mydb = myclient["shuan"]
mycol = mydb["shuan_db"]
mycol.delete_many({}) #drop table

time1 = datetime.datetime.now()

for i in range(10000):
    post = {"where": "shuan","date": datetime.datetime.utcnow()}
    mycol.insert_one(post)
    i+=1
print("total cost :" , datetime.datetime.now() - time1 )


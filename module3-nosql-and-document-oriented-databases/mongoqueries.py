import pymongo


#B_URI = ("mongodb+srv://TerrenceM23:<password>@cluster0-2cfdw.mongodb.net/<dbname>?retryWrites=true&w=majority")



client = pymongo.MongoClient("mongodb+srv://TerrenceM23:<password>@cluster0-2cfdw.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test
db.test.insert_many
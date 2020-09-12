import pymongo
import datetime


class Connection:
    def __init__(self):
        try:
            self.con = pymongo.MongoClient('localhost',27017)
            print('\n\tConnected successflly\n')
            dbs = pymongo.MongoClient().list_database_names()
            print('\n\t',dbs)

        except:
            print("Could not connect to MongoDB")
            
    def myDB(self):
        DB_name = input("\t\nEnter DB_name to use DB\t")
        mydb = self.con[DB_name]
        self.db = mydb
        if mydb:
            print()
            print('\n\t',mydb.list_collection_names())
            col_name = input("\t\nEnter collection name \t")
            self.mycol = mydb[col_name]


    def show(self, keyfield=None , id = None):
        if id is None and keyfield is None:
            return self.mycol.find({})
        else:
            return self.mycol.find({keyfield:id})

    def createData(self,data):
        save = self.mycol.insert_one(data)
        if save:
            return save
        else:
            return None

    def updateData(self,data,pk,pkval):
        filter = { pk: pkval}
        newvalues = { "$set": data }
        save = self.mycol.update_one(filter,newvalues)
        if save:
            return save
        else:
            return None

    def deleteData(self,k=None,v=None):
        if k is None and v is None:
            deleted = self.mycol.delete_many({})
            if deleted:
                return deleted
            else:
                return None
        else:
            filter = {k:v}
            deleted = self.mycol.delete_one(filter)
            if deleted:
                return deleted
            else:
                return None

        

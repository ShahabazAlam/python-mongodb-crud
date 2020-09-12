from connections import Connection
import pymongo
from os import system
from time import sleep
# -------------------------Actions ---------------------
def allActions():
    while(True):
        choice = input('Enter Command\t\n')
        if choice == '1':
            opera.readData()
            break
        if choice == '2':
            opera.create()
            break

        if choice == '3':
            opera.update()
            break
        if choice == '4':
            opera.delete()
            break

        if choice == '5':
            opera.deleteAll()
            break

        elif choice == '6':
            system('cls')
            home.allCommandList()
        elif choice == '7':
            print('*'*10 ,"Thanks For Using Me" ,'*'*10 )
            sleep(2)
            system('cls')
            break
        else:
            print("Invalid Input")

#---------------Home class ---------------------------
class Home:
    def allCommandList(self): 
        print('''   \n Show all users : 1
                    \n Add new user   : 2
                    \n Update a user  : 3 
                    \n Delete a user  : 4
                    \n Del all users  : 5
                    \n Clear Screen   : 6
                    \n Exit           : 7
            \n ''')

class Operations:
    def readData(self):
        system('cls')
        print('''   \n Show all users : 1
                    \n Show a users   : 2
                    \n Clear Sceern   : 3
                    \n Exit           : 4
                ''')

        command = input('Enter command\t')
        if command == '1':
            users = mycon.show()
            if users != None:
                for d in users:
                    print('\t:',d,'\n')
                confirm = input('For continue press any key \t')
                if confirm:
                    system('cls')
                    opera.readData()
            else:
                print("No data found!")

        elif command == '2':
            k = input('Enter key\t')
            v = input('Enter Value\t')
            user = mycon.show(k,v)
            if user != None:
                for d in user:
                    print('\t:',d,'\n')
            else:
                print("Not found please enter correct key & value!")
            confirm = input('For continue press any key \t')
            if confirm:
                system('cls')
                opera.readData()

        elif command == '3':
            system('cls')
            opera.readData()

        elif command == '4':
            system('cls')
            home.allCommandList()
            allActions()

    def create(self):
        mylist = []
        while(True):
            k = input('Enter Key\t')
            v = input('Enter Value\t')
            mylist.append((k,v))
            choice = input('For another field\t\n')
            if choice == 'n' or choice == 'N':
                break
        saved = mycon.createData(dict(mylist))
        if saved:
            print('Saved successfully',saved)
        confirm = input('For create new press any key \n For Home press 1\t')
        if(confirm == 'h' or confirm == 'H'):
            system('cls')
            home.allCommandList()
            allActions()
        else:
            opera.create()

    def update(self):
        mylist = []
        while(True):
            k = input('Enter Key\t')
            v = input('Enter Value\t')
            mylist.append((k,v))
            choice = input('For another field\t\n')
            if choice == 'n' or choice == 'N':
                break

        pk = input('Enter pk for value you want to update')
        pkval = input('Enter pkvalue for value you want to update')

        saved = mycon.updateData(dict(mylist),pk,pkval)
        if saved:
            print('Updated successfully',saved)
        confirm = input('For Update new press any key \n For Home press H\t')
        if(confirm == 'h' or confirm == 'H'):
            system('cls')
            home.allCommandList()
            allActions()
        else:
            opera.update()


    def delete(self):

        k = input('Enter Key\t')
        v = input('Enter Value\t')
        deleted = mycon.deleteData(k,v)
        if deleted:
            print('Deleted successfully',deleted)
        confirm = input('For Delete new press any key \n For Home press H\t')
        if(confirm == 'h' or confirm == 'H'):
            system('cls')
            home.allCommandList()
            allActions()
        else:
            opera.delete()

    def deleteAll(self):
        confirm = input('Confirm delete all data!')
        if(confirm == 'y' or confirm == 'Y'):
            deleted = mycon.deleteData()
            if deleted:
                print('Deleted successfully',deleted)
            print('Wait for Home')
            sleep(2)
            system('cls')
            home.allCommandList()
            allActions()
        else:
            system('cls')
            home.allCommandList()
            allActions()


#-------------Connection Methods ----------------
mycon = Connection()
opera = Operations()
mycon.myDB()
home = Home()
home.allCommandList()
allActions()
#-------------Operations Methods ----------------

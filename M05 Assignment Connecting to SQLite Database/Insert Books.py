import sqlite3

indbs=sqlite3.connect("IndianBookstore.db")

ibcursor=indbs.cursor()

ibcursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Books' ''')

if ibcursor.fetchone()[0]!=1:
    ibcursor.execute("CREATE TABLE Books (Accno INTEGER PRIMARY KEY, Title STRING NOT NULL, Author STRING NOT NULL, Price REAL NOT NULL);")

else:
    print("Books table already exists!")
    #ADD NEW RECORDS TO BOOKS TABLE
    while True:
        res=input("Do you want to add new books to the database (Y/N): ")

        if res=='Y' or res=='y':
            accno=int(input("Enter Accno: "))
            title=input("Enter Title: ")
            author=input("Enter Author: ")
            price=float(input("Enter Price: "))

            inssql="INSERT INTO Books (Accno, Title, Author, Price) VALUES ("+str(accno)+",'"+title+"','"+author+"',"+str(price)+");"
            
            try:
                ibcursor.execute(inssql)
                indbs.commit()
                print("Inserted successfully!")

            except:
                print("Error while inserting!")
                indbs.rollback()
        else:
            break

indbs.close()       
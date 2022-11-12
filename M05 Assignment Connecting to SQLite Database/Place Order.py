import sqlite3

indbs=sqlite3.connect("IndianBookstore.db")
ibcursor=indbs.cursor()

total=0

while True:
    title=input("\nEnter title of the book: ")
    try:
        ibcursor.execute("SELECT * FROM Books where Title='"+title+"'")
        record=ibcursor.fetchall()
        if len(record)==0:
            print("No such book exists!")
            continue
        else:
            print(record)
    except:
        print("Error while executing!")
        indbs.rollback()
    copies=int(input("Enter the number of copies: "))
    total=total+record[0][3]*copies

    yn=input("Do you want to place order for another book (Y/N): ")
    if yn=='Y' or yn=='y':
        continue
    else:
        break
print("Total price: "+str(total))
indbs.close()
from tkinter import *
import mysql.connector
from datetime import datetime
#pip install -U httpcore httpx
def insert():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
            user="root",
            passwd="Admin",
            database="product",
            auth_plugin='mysql_native_password'
        )
        product_name=entry_productname.get()
        qty=int(entry_qty.get())
        price=int(entry_price.get())

        cursor=mydb.cursor()

        cursor.execute("insert into product (product_name,qty,price) values (%s,%s,%s)",(product_name,qty,price))
        print("data inserted successfully")
        mydb.commit()
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
        
def show():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
            user="root",
            passwd="Admin",
            database="product",
            auth_plugin='mysql_native_password'
        )
        cursor=mydb.cursor()
        cursor.execute("select * from product")
        db=cursor.fetchall()
        if db:
            for i in db:
                show_label.config(i)
    except mysql.connector.Error as err:
        print(f"error:{err}")
        show_label.config(f"error:{err}")
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
        
def sale():
    product1=input("enter product")

root=Tk()
root.title("Inventory management System")
label_productname=Label(root,text="product name")
label_productname.grid(row=0,column=0,padx=10,pady=10)
entry_productname=Entry(root)
entry_productname.grid(row=0,column=1,padx=10,pady=10)
label_qty=Label(root,text="Quantity")
label_qty.grid(row=1,column=0,padx=10,pady=10)
entry_qty=Entry(root)
entry_qty.grid(row=1,column=1,padx=10,pady=10)
label_price=Label(root,text="price")
label_price.grid(row=2,column=0,padx=10,pady=10)
entry_price=Entry(root)
entry_price.grid(row=2,column=1,padx=10,pady=10)
insert=Button(root,text="Insert")
show=Button(root,text="show",command=show())
#show label
show_label=Label(root,text="")
show_label.grid(row=6,column=0,padx=10,pady=10)
root.mainloop()    
        
    
    



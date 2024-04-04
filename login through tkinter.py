import mysql.connector
from tkinter import*
def register_user():
    print("Registration Form")
    username=entry_username.get()
    password=entry_password.get()
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="Admin@123",database="atmosphere_metric",auth_plugin='mysql_native_password')
        if mydb.is_connected():
            print("connected")
            cursor=mydb.cursor()
            query1="insert into login_user (username,password) values(%s,%s)"
            cursor.execute(query1,(username,password))
            mydb.commit()
    except mysql.connector.Error as err:
        print(err)
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            print("connection closed")
def login_user():
        username=entry_username.get()
        password=entry_password.get()
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="Admin@123",database="atmosphere_metric",auth_plugin='mysql_native_password')
            if mydb.is_connected():
                print("connected")
                cursor=mydb.cursor()
                query2="select * from login_user where username=%s and password=%s"
                cursor.execute(query2,(username,password))
                result=cursor.fetchone()
                if result:
                    msg_label.config(text="Login sucessfull")
                else:
                    msg_label.config(text="iNvalid username or password")
                mydb.commit()
        except mysql.connector.Error as err:
            print(err)
        finally:
            if 'mydb' in locals() and mydb.is_connected():
                mydb.close()
                print("connection closed")

#create tkinter window
root=Tk()
root.title("Registartion Form")
#Registration Section
label_username=Label(root,text="Username")
label_username.grid(row=0,column=0,padx=10,pady=10)
entry_username=Entry(root)
entry_username.grid(row=0,column=1,padx=10,pady=10)
label_password=Label(root,text="password")
label_password.grid(row=1,column=0,padx=10,pady=10)
entry_password=Entry(root)
entry_password.grid(row=1,column=1,padx=10,pady=10)
button_login=Button(root,text="submit",command=register_user)
button_login.grid(row=4,column=0,columnspan=2,pady=10)
button_login=Button(root,text="login",command=login_user)
button_login.grid(row=4,column=1,columnspan=2,pady=10)
#message label
msg_label=Label(root,text="")
msg_label.grid(row=6,column=0,columnspan=2,pady=10)
#start tkinter
root.mainloop()

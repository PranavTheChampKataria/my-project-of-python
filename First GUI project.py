from tkinter import *
import os
import fileinput
class user_credentials():
    Login_ = False
    current_balance = 0
    name = "jayesh"
    password = "_"
    new_login_name = "kau"
    new_login_password = "_"

def online():

    root_netbanking = Tk()
    root_netbanking.title("Net Banking")
    root_netbanking.geometry("300x100")
    root_netbanking.configure(bg="black")

    def Login():
        # root_netbanking5.destroy()
        # root_netbanking7.destroy()
        root_netbanking1 = Tk()
        root_netbanking1.title("Login")
        root_netbanking1.geometry("300x150")

        lab1 = Label(root_netbanking1, text="User name:", font=("arial",10,"bold"))
        lab1.pack()
        
        user_name = StringVar()
        user_credentials.name = Entry(root_netbanking1, textvariable="user_name", bg="white", fg="black", width="25")
        user_credentials.name.pack()

        lab2 = Label(root_netbanking1, text="User password:", font=("arial",10,"bold"))
        lab2.pack()
        
        user_password = StringVar()
        user_credentials.password = Entry(root_netbanking1, textvariable="user_password", bg="white", fg="black", width="25")
        user_credentials.password.pack()

        def Login_done():
            user_credentials.name     = str(user_credentials.name.get())
            user_credentials.password = str(user_credentials.password.get())
            userfile = open("C:\\Users\\Shweta\\Documents\\python pro\\" + user_credentials.name, "r")
            content1 = userfile.read(6)
            print(content1)
            if( os.path.exists("C:\\Users\\Shweta\\Documents\\python pro\\" + user_credentials.name) and
            user_credentials.password == content1):
                os.system("cls")
                userfile.close()
                user_credentials.Login_ = True
                root_netbanking.destroy()
                root_netbanking1.destroy()
                root_netbanking2 = Tk()
                root_netbanking2.title("Login successfully")
                root_netbanking2.geometry("300x200")

                def check_balance():
                    os.system("cls")
                    userfile = open("C:\\Users\\Shweta\\Documents\\python pro\\" + user_credentials.name, "r")
                    content  = userfile.read()
                    print(content)
                    userfile.close()
                    
                button5 = Button(root_netbanking2, text="Check balance", width=25, height=2, bg="blue", fg="white", command=check_balance)
                button5.place(x=54, y=5)

                def deposite_money():
                    root_netbanking4 = Tk()
                    root_netbanking4.title("Deposite money")
                    root_netbanking4.geometry("300x150")
                    root_netbanking4.configure(bg="black")
                    lab4 = Label(root_netbanking4 , text="Deposite here: ", font=("arial",15,"bold"), bg="black",fg="white")
                    lab4.pack()
                    deposite_money = IntVar()
                    entry3 = Entry(root_netbanking4,textvariable="deposite_here", width=25, bg="white",fg="black")
                    entry3.pack()

                    def done_deposite():
                        os.system("cls")
                        user_credentials.current_balance = user_credentials.current_balance + int(entry3.get())
                        userfile = open("C:\\Users\\Shweta\\Documents\\python pro\\" + user_credentials.name, "a")
                        userfile.write("\nYour balance is: " +str(user_credentials.current_balance))
                        userfile.close()
                        lab3 = Label(root_netbanking4 , text="Your new deposite is: " + str(user_credentials.current_balance),
                        font=("arial",15,"bold"), bg="black",fg="white")
                        lab3.place(x=10, y=120)
                        entry3.delete(0,"end")
                        print("hello")

                    button10 = Button(root_netbanking4, text="Enter", width=10, height=1, bg="blue", fg="white", command=done_deposite)
                    button10.place(x=110, y=55)

                    def exit_Current_balance():
                        root_netbanking4.destroy()

                    button10 = Button(root_netbanking4, text="Exit", width=10, height=1, bg="blue", fg="white", command=exit_Current_balance)
                    button10.place(x=110,y=85)
                    root_netbanking4.mainloop()

                button6 = Button(root_netbanking2, text="Deposite money", width=25, height=2, bg="blue", fg="white", command=deposite_money)
                button6.place(x=54, y=50)

                def manage_account():
                    root_netbanking2.destroy()
                    root_netbanking5 = Tk()
                    root_netbanking5.title("Manage account")
                    root_netbanking5.geometry("300x120")
                    root_netbanking5.configure(bg="black")

                    def change_name():
                        root_netbanking6 = Tk()
                        root_netbanking6.title("Change user name")
                        root_netbanking6.geometry("300x120")

                        lab7 = Label(root_netbanking6, text="Enter user name", font=("arial",10,"bold"))
                        lab7.pack()

                        change_name_entry = StringVar()
                        entry4 = Entry(root_netbanking6, text="change_name_entry", bg="white", fg="black", width="25")
                        entry4.pack()

                        def save_name():
                            os.system("cls")
                            new_name = entry4.get()
                            os.rename(user_credentials.name,new_name)
                            print("Your  new name is: " + new_name)
                            root_netbanking5.destroy()
                            root_netbanking6.destroy()
                            online()
                        button12 = Button(root_netbanking6, text="save", width=10, bg="blue", fg="white", command=save_name)
                        button12.pack()

                    button11 = Button(root_netbanking5, text="Change user name", width=40,height=2, bg="blue", fg="white", command=change_name)
                    button11.place(x=5,y=10)

                    def change_password():
                        root_netbanking7 = Tk()
                        root_netbanking7.title("Change password name")
                        root_netbanking7.geometry("300x120")
                        
                        lab8 = Label(root_netbanking7, text="Enter password", font=("arial",10,"bold"))
                        lab8.pack()

                        change_password_entry = StringVar()
                        entry5 = Entry(root_netbanking7, text="change_password_entry", bg="white", fg="black", width="25")
                        entry5.pack()
                        
                        def save_password():
                            os.system("cls")
                            user_credentials.password = str(entry5.get())
                            userfile2 = open("C:\\Users\\Shweta\\Documents\\python pro\\" + user_credentials.name, "r")
                            fline = user_credentials.password
                            oline = userfile2.readlines()
                            oline.insert(0,fline)
                            userfile2.close()

                            userfile2 = open("C:\\Users\\Shweta\\Documents\\python pro\\" + user_credentials.name, "w")
                            userfile2.writelines(oline)
                            userfile2.close()
                            print("Your new password is: " + user_credentials.password)
                            root_netbanking5.destroy()
                            root_netbanking7.destroy()
                            online()
                        button13 = Button(root_netbanking7, text="save", width=10, bg="blue", fg="white", command=save_password)
                        button13.pack()

                    button11 = Button(root_netbanking5, text="Change password", width=40,height=2, bg="blue", fg="white", command=change_password)
                    button11.place(x=5,y=60)

                    root_netbanking5.mainloop()

                button7 = Button(root_netbanking2, text="Manage account", width=25, height=2, bg="blue", fg="white", command=manage_account)
                button7.place(x=54, y=95)

                def exit_login():
                    user_credentials.Login_ = False
                    root_netbanking2.destroy()
                button8 = Button(root_netbanking2, text="Exit", width=25, height=2, bg="blue", fg="white", command=exit_login)
                button8.place(x=54, y=140)  
                root_netbanking2.mainloop()
            
            else:
                user_credentials.Login_ = False
                print("wrong username or password!")
        button4 = Button(root_netbanking1, text="Done", width=10, bg="blue", fg="white", command=Login_done)
        button4.place(x=62, y=85)

        def Exit():
            root_netbanking1.destroy()
        button3 = Button(root_netbanking1, text="Exit", width=10, bg="blue", fg="white", command=Exit)
        button3.place(x=155, y=85)
        root_netbanking1.mainloop()
        

    button1 = Button(root_netbanking, text="Login", width=25, height=2, bg="blue", fg="white",command=Login)
    button1.place(x=54, y=5)

    def New_account():
        root_netbanking8 = Tk()
        root_netbanking8.title("New account")
        root_netbanking8.geometry("300x120")
        root_netbanking8.configure(bg="black")
        lab9 = Label(root_netbanking8, text="Enter User name:", font=("arial",10,"bold"))
        lab9.pack()  
        user_name_here = StringVar()
        user_credentials.name = Entry(root_netbanking8, textvariable="user_name_here", bg="white", fg="black", width="25")
        user_credentials.name.pack()

        lab10 = Label(root_netbanking8, text="User password:", font=("arial",10,"bold"))
        lab10.pack()
        user_password_here = StringVar()
        user_credentials.password = Entry(root_netbanking8, textvariable="user_password_here", bg="white", fg="black", width="25")
        user_credentials.password.pack()

        def save_new_account():
            os.system("cls")
            user_credentials.Login_   = True  
            user_credentials.name     = str(user_credentials.name.get())
            user_credentials.password = str(user_credentials.password.get())
            userfile  = open("C:\\Users\\Shweta\\Documents\\python pro\\" + user_credentials.name, "w+")
            userfile.write(user_credentials.password)
            userfile.write("\nHi " + user_credentials.name)
            userfile.write("\nYour balance is: " + str(user_credentials.current_balance))
            print("Successfull")


        button14 = Button(root_netbanking8, text="save", width=10, bg="blue", fg="white", command=save_new_account)
        button14.pack()
        root_netbanking8.mainloop()

    button2 = Button(root_netbanking, text="New account", width=25, height=2, bg="blue", fg="white", command=New_account)
    button2.place(x=54, y=50)

    root_netbanking.mainloop()
online()
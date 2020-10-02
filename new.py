from tkinter import *
import random
from datetime import datetime
import tkinter.font as TkFont
import time
from tkinter import messagebox as msg
from win32com.client import Dispatch

root = Tk()
root.geometry("700x600")
root.title("WebdoWs")
root.configure(bg="MediumPurple4")

def login():
    name_e.destroy()
    email_e.destroy()
    name.destroy()
    email.destroy()
    password.destroy()
    password_e.destroy()
    submit.destroy()
    login.destroy()

    def entring():
        pass

    def back():
        name_id.destroy()
        name_id_e.destroy()
        email_password.destroy()
        email_password_e.destroy()
        enter.destroy()
        back.destroy()
        captcha.destroy()

        # label name, email, password, recaptcha(radiobutton)
        # frame for name , email, password
        # fra4 = Frame(root, bg="MediumPurple4")
        name1 = Label(fra, text="Enter name:", font="arial 10 bold", bg="MediumPurple4", fg="white")
        email1 = Label(fra,text="Enter email:", font="arial 10 bold", bg="MediumPurple4", fg="white")
        password1 = Label(fra, text="password:", font="arial 10 bold", bg="MediumPurple4", fg="white")

        # entry name, email, password
        name_e1 = Entry(fra, textvar=StringVar(), bg="MediumPurple1", font="arial 10 bold")
        email_e1 = Entry(fra, textvar=StringVar(), bg="MediumPurple1", font="arial 10 bold")
        password_e1 = Entry(fra, textvar=StringVar(), bg="MediumPurple1", font="arial 10 bold")

        # frame for submit and login button
        # fra1 = Frame(root, bg="MediumPurple4")
        submit1 = Button(fra1, text="Submit", font="arial 10 bold", padx=5, command=submiting, bg="dark violet", fg="white", borderwidth=1)
        login1 = Button(fra1, text="Login", font="arial 10 bold", padx=5, command=login, bg="dark violet", fg="white", borderwidth=1, width=7)
        captcha1 = Radiobutton(root, text="i am not a Bot", font="arial 10 bold", bg="MediumPurple4", fg="black", borderwidth=2)


        # label widgets
        name1.grid(row=1, column=0, pady = 15, padx = 4)
        email1.grid(row=2, column=0, pady=15, padx = 4)
        password1.grid(row=3, column=0, pady=15, padx = 4)
        # entry widgets
        name_e1.grid(row=1, column=1, pady=6, ipadx=20)
        email_e1.grid(row=2, column=1, pady=6, ipadx=20)
        password_e1.grid(row=3, column=1, pady=6, ipadx=20)
        # fra4.pack()
        # button widgets
        submit1.grid(row=1, column=0, padx=5, pady=2)
        login1.grid(row=1, column=1, pady=2)
        captcha1.pack(padx=20, pady=8)
        # fra1.pack()


    # labels for the name and password
    name_id = Label(fra, text="User name:", font="arial 10 bold", bg="MediumPurple4", fg="white")
    email_password = Label(fra, text="Email Password:", font="arial 10 bold", bg="MediumPurple4", fg="white")

    # entry widget for name and password
    name_id_e = Entry(fra, textvar=StringVar(), bg="MediumPurple1", font="arial 10 bold")
    email_password_e = Entry(fra, textvar=StringVar(), bg="MediumPurple1", font="arial 10 bold")

    # making button for entre the information(name, password) and a back button
    enter = Button(fra1, text="Enter", font="arial 10 bold", padx=5, command=entring, bg="dark violet", fg="white", borderwidth=1)
    back  = Button(fra1, text="Back", font="arial 10 bold", padx=5, command=back, bg="dark violet", fg="white", borderwidth=1)


    if __name__ == "__main__":
        name_id.grid(row=1, column=1, pady=5)
        name_id_e.grid(row=1, column=2)

        email_password.grid(row=2, column=1, pady=7)
        email_password_e.grid(row=2, column=2)

        enter.grid(row=1 ,column=0, padx=5, pady=2)
        back.grid(row=1, column=1, pady=2)



def openNewWindow():
    '''
    make a file with the name entered by the user in name widget
    and store all the infomation into the file like:- name, email and password
    '''
    with open(f"{name_e.get()}.txt", "w") as f:
        f.write(f"{password_e.get()}\nEmail is {email_e.get()}\nName is {name_e.get()}")

    statusbar.set("submited !")
    status_bar.update()
    time.sleep(1.5)

    statusbar.set("Opening new window...")
    status_bar.update()

    def speak(str):
        '''
        a function that converts an string into
        a audio
        '''
        speak = Dispatch("SAPI.spVoice")
        speak.Speak(str)

    # destroying the pervious window
    root.destroy()
    # making a new window
    rootNew = Tk()
    rootNew.geometry("500x450")
    rootNew.title("WebdoWs")
    rootNew.configure(bg="MediumPurple4")

    if __name__ == "__main__":
        # label of introduction
        intro_l = Label(rootNew, text="Hi...", bg="MediumPurple4", fg="white", font="lucida 15 bold")
        intro_l1 = Label(rootNew, text="MY Name is univer", bg="MediumPurple4", fg="white", font="lucida 15 bold")
        end_intro = Label(rootNew, text="I am a AI Robot", bg="MediumPurple4", fg="white", font="lucida 15 bold")

        # packing the labels(introductions)
        speak("Hi my name is univer and i programmed by jayesh kaushik")
        intro_l.pack()
        intro_l1.pack()
        end_intro.pack()




def event(event):
    pass

def submiting():
    '''
    check that the information is correct, filled or not
    if not filled ask for exit(yes or not) 
    if not correct clear all the widgets(name, email, password)
    if correct then call the openNewWindow():- function
    '''
    try:
        if name_e.get() == "" or email_e.get() == "" or password_e.get() == "":
        
            statusbar.set("Please fill all the entries : Name, Email and Password.")
            status_bar.update()
            time.sleep(2.5)

            statusbar.set("Ready...")
            status_bar.update()
            value1 = msg.askyesno("Help", "Do you want to Exit!")
            if value1 is True:
                exit()
            else:
                name_e.delete(0, END)
                email_e.delete(0, END)
                password_e.delete(0, END)
               

        else:
            # confromation for the submited information is correct or not
            value = msg.askyesno("Help", f"name:{name_e.get()}\nemail:{email_e.get()}\npassword:{password_e.get()}\n\nInformation is correct or not?")
            if value is True:
                statusbar.set("submiting...")
                status_bar.update()

                time.sleep(1.5)

                statusbar.set("Submited!")
                status_bar.update()
                openNewWindow()
            else:
                name_e.delete(0, END)
                email_e.delete(0, END)
                password_e.delete(0, END)

    except Exception as e:
        print(name_e1.get())
        if name_e1.get() == "" or email_e1.get() == "" or password_e1.get() == "":
            statusbar.set("Please fill all the entries : Name, Email and Password.")
            status_bar.update()
            time.sleep(2.5)

            statusbar.set("Ready...")
            status_bar.update()
            value2 = msg.askyesno("Help", "Do you want to Exit!")
            if value2 is True:
                exit()
            else:
                name_e1.delete(0, END)
                email_e1.delete(0, END)
                password_e1.delete(0, END)

        else:
            # confromation for the submited information is correct or not
            value = msg.askyesno("Help", f"name:{name_e1.get()}\nemail:{email_e1.get()}\npassword:{password_e1.get()}\n\nInformation is correct or not?")
            if value is True:
                statusbar.set("submiting...")
                status_bar.update()

                time.sleep(1.5)

                statusbar.set("Submited!")
                status_bar.update()
                openNewWindow()
            else:
                name_e1.delete(0, END)
                email_e1.delete(0, END)
                password_e1.delete(0, END)



if __name__ == "__main__":

    # label the heading
    head_frame = Frame(root)
    head = PhotoImage(file="head.png")
    # heading = Label(root, text="Welcome to Webdows", relief=SUNKEN, font="lucida 20 bold", bg="purple1", fg="white", borderwidth=2)
    heading = Label(head_frame, image=head, bg="MediumPurple4", pady=50)

    # label the status bar
    statusbar = StringVar()
    statusbar.set("Ready")
    # my sign to the statusbar label
    # statusbar_permanent.set("Designed by Jayesh kaushik...")
    status_bar = Label(root, textvar=statusbar, relief=SUNKEN, anchor="w", bg="Purple4", fg="white", font="lucida 9 ")

    # label name, email, password, recaptcha(radiobutton)
    # frame for name , email, password
    fra = Frame(root, bg="MediumPurple4")
    name = Label(fra, text="Enter name:", font="arial 10 bold", bg="MediumPurple4", fg="white")
    email = Label(fra,text="Enter email:", font="arial 10 bold", bg="MediumPurple4", fg="white")
    password = Label(fra, text="password:", font="arial 10 bold", bg="MediumPurple4", fg="white")

    # frame for submit and login button
    fra1 = Frame(root, bg="MediumPurple4")
    submit = Button(fra1, text="Submit", font="arial 10 bold", padx=5, command=submiting, bg="dark violet", fg="white", borderwidth=1)
    login_text = StringVar()
    login_text.set("Login")
    login = Button(fra1, textvar=login_text, font="arial 10 bold", padx=5, command=login, bg="dark violet", fg="white", borderwidth=1, width=7)
    captcha = Radiobutton(root, text="i am not a Bot", font="arial 10 bold", bg="MediumPurple4", fg="black", borderwidth=2)

    # entry name, email, password
    name_e = Entry(fra, textvar=StringVar(), bg="MediumPurple1", font="arial 10 bold")
    email_e = Entry(fra, textvar=StringVar(), bg="MediumPurple1", font="arial 10 bold")
    password_e = Entry(fra, textvar=StringVar(), bg="MediumPurple1", font="arial 10 bold")

    # making a frame for the photo of webdows
    '''
    this i can use later
    to make new window of my software
    '''
    photo_frame = Frame(root)
    photo = PhotoImage(file="web1.png")
    photo_label = Label(photo_frame, image=photo, bg="MediumPurple4", pady=50)



    # griding the name, password, email, captcha, heading, status_bar
    heading.pack(fill=X, side=TOP)
    head_frame.pack()

    name.grid(row=1, column=0, pady = 15, padx = 4)
    email.grid(row=2, column=0, pady=15, padx = 4)
    password.grid(row=3, column=0, pady=15, padx = 4)

    name_e.grid(row=1, column=1, pady=6, ipadx=20)
    email_e.grid(row=2, column=1, pady=6, ipadx=20)
    password_e.grid(row=3, column=1, pady=6, ipadx=20)
    fra.pack()

    submit.grid(row=1, column=0, padx=5, pady=2)
    login.grid(row=1, column=1, pady=2)
    fra1.pack()
    


    captcha.pack(padx=20, pady=8)

    status_bar.pack(fill=X, side=BOTTOM)

    
    root.mainloop()
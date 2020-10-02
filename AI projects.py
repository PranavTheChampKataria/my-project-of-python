from tkinter import * # this is used for to make the window
from win32com.client import Dispatch # this is used for to make a speak function which converts the string into audio
from PIL import Image, ImageTk # this is used for to display the images(in jpg form and also png form) and also used for resizing the images
from playsound import playsound # This module is used to play the mp3 sound
import speech_recognition as sr # this module is used to recognize the speech said by the user
import webbrowser # this module is used for  open the google.com and youtube.com
import os

run_app = True# Initializing the end program
root_window = Tk() # Initializing the window
root_window.geometry("400x500") # Width x height
root_window.maxsize(400,500)
root_window.configure(bg="black") # Colour of background is black
root_window.title("Anonymous app") # Title of the window
photo = PhotoImage(file="anon.png") # Photo for the icon of the tkinter window
root_window.iconphoto(FALSE, photo) # For icon photo

# this label is used for print the anonymous
l_for_anonymous = Label(root_window, text="ANONYMOUS", bg="black", fg="White", font=("Symbol", 25))
l_for_anonymous.pack()

# this label is used for the photo
im = Image.open("anon.png")
new_size = im.resize((50, 50))
photo_in = ImageTk.PhotoImage(im)
l_for_Photo_in = Label(root_window, image=photo_in, borderwidth=0)
l_for_Photo_in.pack()

# INitializing the speak function which takes the string as an input and convert into audio
def speak(str):
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            print("Recognizing...")
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en=in")
            print(f"Did you mean:{query}")
        except Exception as e:
            return "none"
        return query

def login():
    '''
    first show the button to continue with id
    second username and password
    '''
    b_for_login.pack_forget()
    b_for_sign_email.pack_forget()
    l_for_or.pack_forget()
    
    # this label is used for label the username
    l_for_username = Label(root_window, text="User name:", bg="black", fg="white", font="arial 10 bold")
    l_for_username.pack()
    # this label is used for entry of username
    e_for_username = Entry(root_window, textvariable=StringVar, bg="light coral")
    e_for_username.pack()

    # this label is used for label the userpassword
    l_for_userpassword = Label(root_window, text="User password:", bg="black", fg="white", font="arial 10 bold")
    l_for_userpassword.pack()
    # this label is used for entry of userpassword
    e_for_userpassword = Entry(root_window, textvariable=StringVar, bg="aquamarine")
    e_for_userpassword.pack()

    def submit():
        if e_for_username.get() == "uni-ver" and e_for_userpassword.get() == "572303":
            speak(f"welcome {e_for_username.get()}")
            speak("How are you")
            while True:
                query = take_command().lower()
                if"i am fine" in query:
                    speak("Ok Sir.. so what is the command for me")
                elif "open youtube" in query:
                    webbrowser.open("youtube.com")
                elif "open google" in query:
                    webbrowser.open("google.com")
                elif "open instagram" in query:
                    webbrowser.open("instagram.com")
                elif "play music" in query:
                    # TODO: TO play the music
                    pass
                
        else:
            playsound('anon laugh.mp3')
            exit()

    # button for submit the username and userpassword
    b_for_submit = Button(root_window, text="Submit",  bg="blue violet", fg="white", font="Courier 15", command=submit)
    b_for_submit.pack()


# this button is used for login
b_for_login = Button(root_window, text="Log In", bg="blue violet", width=10, fg="white", font="Courier 15", command=login)
b_for_login.pack()

# this label is used for print the or
l_for_or = Label(root_window, text="----------- or -----------", bg="black", fg="grey", font=("Times", 25))
l_for_or.pack()

def login_email():
    print("Login successfully.")
# this button is used for login with email
b_for_sign_email = Button(root_window, text="Sign up with email", bg="blue violet", fg="white", font="Courier 15", command=login_email)
b_for_sign_email.pack()


root_window.mainloop()
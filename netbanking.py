### net banking project ###

import os


class User_Credentials():
  login = False
  current_balance = 0
  name = "jayesh"
  root_password = "-"

def main():
  print("""

press 1 - Account status
press 2 - Withdrawl
press 3 - Deposite
press 4 - Manage account
press 5 - Logout  
  """)

  j = int(input(">"))


  if(j == 1):
    os.system("cls")
    print("Your account balance is :",User_Credentials.current_balance)
    main()

  elif(j == 2):
    os.system("cls")
    Withdrawl()
    main()

  elif(j == 3):
    os.system("cls")
    added_money = int(input("How much money you wanted to deposite : "))
    User_Credentials.current_balance += added_money
    print("your New balance is : ",User_Credentials.current_balance)
    main()

  elif(j == 4):
    os.system("cls")
    print("Hi " + User_Credentials.name)
    
    
    print("""
press 1 for Change Username    
press 2 for Change password
    """)

    k = int(input(">"))

    if(k == 1):
      User_Credentials.name = input("Enter your New name : ")
      print("New user name is " + User_Credentials.name)
      main()
    elif(k == 2):
      User_Credentials.root_password = input("Enter your New password")
      print("New password is " + User_Credentials.root_password)
      main()
    else:
      main()

def Withdrawl():
  ask = int(input("How much money you wanted to withdrawl : "))
  
  if(User_Credentials.current_balance == 0):
    print("You can't withdrawl money")
    print("Your current_balance is : ", User_Credentials.current_balance)
  elif(User_Credentials.current_balance >= 0):
    print("Your current balance is : ",User_Credentials.current_balance - ask)
  else:
    online()


def New_account():
  os.system('cls')
  User_Credentials.name = input("Enter your name : ")
  User_Credentials.root_password = input("enter your password : ")
  User_Credentials.login = True
  user   = open("C:\\Users\\Shweta\\Desktop\\Netbanking\\" + User_Credentials.name, "w+")
  user.write(User_Credentials.root_password)
  main()

def login():
  os.system('cls')
  un = input("Enter your name : ")
  if(os.path.exists("C:\\Users\\Shweta\\Desktop\\Netbanking\\" + un)):
    userFile = open("C:\\Users\\Shweta\\Desktop\\Netbanking\\" + un, "r")
    # userFile.write("your current abalance is :" + str(User_Credentials.current_balance))
    p = input("password : ")

    content = userFile.read()
    password = content.split()
    if(p == password[0]):
      userFile = open("C:\\Users\\Shweta\\Desktop\\Netbanking\\" + un, "w+")

      main()
    else:
      print("press 1 for Try again!")
      num = int(input("\n>"))
      if(num == 1):
        login()
      else:
        online()

  else:
    online()




def online():
  print("""
press 1 - Login
press 2 - New account
press 3 - Exit
  """)

  i = int(input(">"))


  if(i == 1):
    login()
  elif(i == 2):
    New_account()
  elif(i == 3):
    os.system("cls")
    input("<>")
  else:
    print("Invalid input!")
    online()
    

online()


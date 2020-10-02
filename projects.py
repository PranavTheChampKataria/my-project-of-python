# Python problem 2
'''
This program tell us that in how many ways can the apples(inputed by the user) can 
be distributed in between minimum and maximum number of sutdents
'''
# try:
#     num = int(input("Enter the number of apples:"))
#     mn = int(input("Enter the Minimum number of students:"))
#     mx = int(input("Enter the Maximum number of students:"))
#     if mn < mx :
#         for i in range(mn,mx+1):
#             if(num%i == 0):
#                 print(f"{i} is a divisor of {num}")
#             else:
#                 print(f"{i} is not a divisor of {num}")

#     elif(mn > mx):
#         print("\nThis is not a range!\nMaximum number of students is greater then Minimum number of students.")
#     elif(mn == mx):
#         print("\nThis is not a range!\nMaximum number of students is equal to Minimum number of students.")

# except Exception as e:
#     print("Your input is wrong!")






# Python problem 3
# '''
# This program take length of the list
# and then ask for the calories to the length times
# and then the program reversed the list by three different
# and check that form all three method the reversed list is same
# or not if all are same then print All are same
# '''
# # Take number of elements in list
# size = int(input("Enter the size of list:\n"))
# # run to the number of elements

# mylist = []
# for i in range(size):
# # Take the elements in the list
#     mylist.append(int(input("Enter the number of calories:")))
# # Print the orignal list
# print(f"your list is {mylist}\n")

# # first method to reverse the list
# reverse1 = mylist[:]
# reverse1.reverse()
# print(f"The reversed list by first method is {reverse1}")

# # second method to reverse the list
# reverse2 = mylist[::-1]
# print(f"the reversed list by second method is {reverse2}")

# # third method to reverse the list
# reverse3 = mylist[:]
# '''
# This for loop is run to the len(reverse3//2) becouse
# if we run this loop to the len(reverse3) it rereverse the
# reversed list.
# eg:- [1,2,3,4,5]
# when(len(reverse3)):
# output is the orignal list: [1,2,3,4,5]

# when(len(reverse3)//2):
# output is the reversed list: [5,4,3,2,1]

# Note: This '//' is used to get the integer not a float
# if we use '/' we get an error becouse for loop only take an integer
# '''
# for i in range(len(reverse3)//2):
#     reverse3[i], reverse3[len(reverse3) -i -1] = reverse3[len(reverse3) -i -1], reverse3[i]
# print(f"The reversed list by third method is {reverse3}\n")

# if reverse1 == reverse2 == reverse3:
#     print("ALL are the list is same.")
# else:
#     print("ALL are the list is not same.")





# # Python problem 4
'''
This program take the number of cases
and ask the user for string(input) and returns 
the palindrome string in output(if the input string is a integer)
otherwise only tell us that the input string is a palidrome or not
'''
# # Take number of test cases
# cases =int(input("Enter the number of cases:\n"))
# # Run to the number of cases
# for i in range(cases):
#     # Take a input as a string
#     str1 = input("Enter any string:\n")
#     # Try to covert the string into integer
#     try:
#         if int(str1)-int(str1)==0:
#             # Reverse the integer
#             re = str1[::-1]
#             # if orignal string is equal to the reversed string then print the statement
#             if str1 == re:
#                 print("The input number is a palindrome\n")
#             # if orignal string is not equal to reversed string then for will run to 10000 times
#             else:
#                 # This for loop starts from the input number
#                 for i in range(int(str1),10000):
#                     # Converting the int i to str i
#                     i1 = str(i)
#                     # Converting the str i1 to list i1
#                     lst1 = list(i1)
#                     # When the length of the list is 2
#                     if len(lst1) == 2:   
#                         # if first element is equal to the second element then print the statement
#                         if lst1[0]==lst1[1]:
#                             print(f"The Next palindrome number is:{i}\n")
#                             break
#                     # When the length of the list is 3
#                     elif len(lst1) == 3:
#                         # if the first element is equal to the last element then print the statement
#                         if lst1[0]==lst1[2]:
#                             print(f"The Next palindrome number is:{i}")
#                             break
#                     # When the length of the list is 4
#                     elif len(lst1) == 4:
#                         # if the first element is equal to the last element and 
#                         # second element is equal to the third element then print the statement
#                         if lst1[0]==lst1[3] and lst1[1]==lst1[2]:
#                             print(f"The Next palindrome number is:{i}")
#                             break
#                     else:
#                         continue
# # This Exception is for entring the string in the input
#     except Exception as e:
# # Reverse the input string
#         re1 = str1[::-1]
#         # if string are equal then print the statement else print the another statement
#         if str1 == re1:
#             print("The input string is a palindrome")
#         else:
#             print("The input string is not a palindrome")




# # Python problem 5
'''
This program takes the numbers and stored them into the list
and tell us the new Palindrome list in which the the elements were replaced
by the next palindrome number crossponding to the last number
'''
# # Take number of element
# num_ele = int(input("Enter the length of list:\n"))
# mylist = []
# # This for loop run to the len times and ask numbers as input and put into the list
# for i in range(num_ele):
#     ele = int(input("Enter the number:"))
#     mylist.append(ele)
# print(f"\nYour list is:{mylist}\n")

# #for make the number to the palindrome
# def next_palindrome(n):
#     n = n + 1
#     while not is_palindrome(n):
#         n += 1
#     return n

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

# # My new list for append the values of next palindrome
# new_mylist = []
# for i in range(num_ele):
#     if mylist[i] >= 10:
#         pali_num = next_palindrome(mylist[i])
#         new_mylist.append(pali_num)
#     else:
#         new_mylist.append(mylist[i])

# print(f"The new palindrome list is:{new_mylist}")






# # Python problem 6
'''
This program genrates a random number between the a and b (inputed by the user)
and we have to guess the number
This is a 2 player game
'''
# import random
# a = int(input("Enter the value of a:"))
# b = int(input("Enter the value of b:"))
# count_p1 = 0
# count_p2 = 0
# mylist = []
# # This for loop is used for make the list of the number b/w a and b
# for i in range(a,b+1):
#     mylist.append(i)
# print(mylist)

# # For choosse the random number
# ran_num = random.choice(mylist)

# # For player 1
# print(f"""
# Player 1:
# Please guess the number between {a} and {b}
# """)
# # This loop is repeat untill player 1 finish the game
# while(True):
# # Count the number of turns of palyer of p1
#     count_p1 = count_p1 + 1
#     p1_value = int(input("Enter any number:\n"))
#     if p1_value == ran_num:
#         print(f"Correct, You took {count_p1} trials to guess the number!\n")
#         break
#     elif p1_value > ran_num:
#         print("Wrong, guess a smaller number!\n")
#     else:
#         print("Wrong, guess a greater number!\n")
    
# # For player 2
# print(f"""
# Player 2:
# Please guess the number between {a} and {b}
# """)
# # This loop is repeat until player 2 finish the game
# while(True):
# # Count the number of turns taken by p2
#     count_p2 = count_p2 + 1
#     p1_value = int(input("Enter any number:\n"))
#     if p1_value == ran_num:
#         print(f"Correct, You took {count_p2} trials to guess the number!\n")
#         break
#     elif p1_value > ran_num:
#         print("Wrong, guess a smaller number!\n")
#     else:
#         print("Wrong, guess a greater number!\n")


# # These if else conditions tell us who wins the game or tie
# if count_p1 == count_p2:
#     print(f"The game is tie on {count_p1}")
# elif count_p1 > count_p2:
#     print(f"Player 2 WINS The match!\nBy the lead of {count_p1 - count_p2}")
# elif count_p2 > count_p1:
#     print(f"Player 1 WINS The match!\nBy the lead of {count_p2 - count_p1}")





# # Python problem 7
'''
This program is for searching the string inputed by the user in the given list
This program is working as a search engine
'''
'''
This function takes 2 argguments s1(input given by the user) and s2(Mylist)
words1 is equal to the split of sentence1
words2 is equal to the split of sentence2
the for loop check that there is a matching of sentence1 to the sentence2 or not
if yes then increses the score by one
'''
# def matchingWord(sentence1, sentence2):
#     words1 = sentence1.strip().split(" ")
#     words2 = sentence2.strip().split(" ")
#     score = 0
#     for word1 in words1:
#         for word2 in words2:
#             if word1 == word2:
#                 score += 1
#     return score
# if __name__ == "__main__":
#     query = input("Please input your query string:\n").lower()
#     # My list
#     mylist = ["this is a good boy", "python is amazing", "one",
#               "python may be the most popular language is few years",
#               "python is not a python snake"]

#     # This scores is for providing the string not the list to the matchingWord function
#     scores = [matchingWord(query, element) for element in mylist]
#     '''
#     This is for to get the matchingWord(sentences) of s1 and s2
#     zip is used for combine the scores and mylist in the form of [(scores, 'mylist')] and the reverse=true is used
#     reversing the list(sortsentscore) in decreasing order(by default it's in the increaing order)
#     if sortsent is equal to 0 then print nothing
#     '''
#     sortedsentscore = [sortsent for sortsent in sorted(zip(scores, mylist), reverse=True) if sortsent[0] != 0]

#     print(f"{len(sortedsentscore)} results found:\n")
#     for items, results in sortedsentscore:
#         print(f"{results} with the score of {items}\n")





# # Python problem 8
'''
 This program is for creating a incorrect table of the number inputed by the user
 and the other function tell us where is the position of the index of the wrong number
'''
# import random
# '''
# This function is used for to check that the table is correct or not 
# '''
# def isCorrect(num,mytable):
#     orignal_list = []
#     for i in range(1,11):
#         # append the table to the orignal_list
#         orignal_list.append(num*i)
#         # This loop is used to check compare the mylist and orignal_list
#     for i in range(len(orignal_list)):
#         # If mytable index is not equal to the orignal_list index then print the index number and the wrong number
#         if mytable[i] != orignal_list[i]:
#             print(f"The index of wrong number {mytable[i]} is {i}")

# '''
# This function is used for make the table and place a rnadom number to the random place
# '''
# def rohanTable(num):
#     mytable = []
#     for i in range(1,11):
#         mytable.append(num*i)
#         # This random fuunction is used for the index
#     ran_num = random.randint(2, 9)
#     # This random function is used  for the number
#     mytable[ran_num] = random.randint(num*2, num*9)
#     print(mytable)
    
#     # Ask for tocheck the table that is right or wrong
#     ask = input("""Do you want to check the table:
#     y - yes
#     n - no
#     """).lower()
#     if ask == "y":
#         isCorrect(num, mytable)
#     elif ask == "n":
#         exit()
#     else:
#         print("Not a valid input!")   

# if __name__ == "__main__":
#     try:
#         num = int(input("Enter a number:\n"))
#         rohanTable(num)
#     except Exception as e:
#         print("Please enter a valid input!")






# # Python problem 9
'''
This program is for jumble the words
'''
# import random
# '''
# Author : jayesh kaushik
# program : Jumble words
# Code for : CodeWithHarry(Practice problem 9)
# This function is used for to jumble the words
# '''
# def jumble_word(first_name, lastt_name, number):
#     for i in range(0, number):
#         # Changing the last name
#         joumbled_name = first_name[i]+" "+lastt_name[random.randint(0, number-1)]
#         print(joumbled_name)

# if __name__ == "__main__":
#     # Length of the name list
#     number = int(input("Enter the number of names:\n"))

#     nameList   = []
#     first_name = []
#     lastt_name = []

#     # Asking the name of the friends
#     for i in range(1,number+1):
#         name = input("Enter the name:")
#         # append to the name list
#         nameList.append(name)
    
#     # Spliting the elements of the name list
#     for ele in nameList:
#         split_name = ele.split(" ")
#         # For the first name
#         first_name.append(split_name[0])
#         # For the second name
#         lastt_name.append(split_name[1])

#     jumble_word(first_name, lastt_name, number)






# Python problem 10
'''
This is a program which tell us in which year you become 100 year older
'''
# def main_():
#     age = int(input("Enter your age or year of birth:"))
#     def claculate_year(n):
#         Year = 2020
#         print("Do you want to know in which year you become 100 years older")
#         print("""
#         y - yes
#         n - no""")
#         ask = input(">>")
#         if(ask == "y"):
            
#             if(age>0 and age<=125):
#                 for i in range(n, 101):
#                     years1 = 100 - n
#                 years_take1 = 2020 + years1
#                 print(f"IN {years_take1} you become 100 year older")
#             elif(age>1900 and age<=2020):
#                 years_take = n + 100
#                 print(f"IN {years_take} you become 100 year older")
        
#         elif(ask == "n"):
#             return None
#         else:
#             print("Wrong input! Try again")

#     if(age>0 and age<=125):
#         print("You input your Age!")
#         claculate_year(age)
#     elif(age>1900 and age<=2020):
#         print("You input your Year of birth!")
#         Year = age
#         claculate_year(Year)
#     elif(age>125 or age>2020):
#         print("You entered the wrong Year or Age!")
#         main_()

# main_()
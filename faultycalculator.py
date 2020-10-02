num1 = int(input("enter your first number: ")) '''user input''' 
print(num1)

op = input("enter your operation: ") '''user input'''
print(op)

num2 = int(input("enter your second number: ")) '''user input'''
print(num2)

if(num1 == 56 and op == "+" and num2 == 7): '''checking for values'''
    result = "77"
    print(result)

elif(op == "+"):
    result = num1 + num2
    print(result)

elif(op == "-"):
    result = num1 - num2
    print(result)

elif(op == "*"):
    result = num1 * num2
    print(result)

elif(op == "/"):
    result = num1 / num2
    print(result)

elif(op == "**"):
    result = num1 ** num2
    print(result)

else:
    print("please cheak your operation!")

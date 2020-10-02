num1 = int(input("enter your first number: "))
print(num1)

op = input("enter your operation: ")
print(op)

num2 = int(input("enter your second number: "))
print(num2)

if(num1 == 56 and op == "+" and num2 == 7):
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

    num = int(input("Enter the number of apples:"))
    mn = int(input("Enter the Minimum number of students:"))
    mx = int(input("Enter the Maximum number of students:"))

    if mn < mx :
        for i in range(mn,mx+1):
            if(num%i == 0):
                print(f"{i} is a divisor of {num}")
            else:
                print(f"{i} is not a divisor of {num}")

    elif(mn > mx):
        print("\nThis is not a range!\nMaximum number of students is greater then Minimum number of students.")
    elif(mn == mx):
        print("\nThis is not a range!\nMaximum number of students is equal to Minimum number of students.")

except Exception as e:
    print("Your input is wrong!")


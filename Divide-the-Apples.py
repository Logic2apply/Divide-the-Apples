# Divide the Apples
try:
    n = int(input("\nEnter the number of apples you got\n: "))
    mn = int(input("\nEnter the Minimim number\n: "))
    mx = int(input("\nEnter the Maximum number\n: "))

except Exception as e:
    print("Invalid input! Only integer allowded")
    exit()

def checkdiv():
    if n%mn==0:
        print(f"{mn} is a divisor {n}")
    else:
        # print(f"{mn} is not a divisor of {n}")
        pass

if mn==0 or mx==0 or n==0:
    print("Can't except 0 for apple-min-max!!\n")
    exit()

elif mx>mn:
    print("Maximum n umber should be greater than or equal to minimum number!!")
    exit()

else:
    if mn==mx:
        checkdiv()
    else:
        while mn<=mx:
            checkdiv()
            mn += 1
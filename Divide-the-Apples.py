# Divide the Apples
n = int(input("\nEnter the number of apples you got\n: "))
mn = int(input("\nEnter the Minimim number\n: "))
mx = int(input("\nEnter the Maximum number\n: "))

def checkdiv():
    if n%mn==0:
        print(f"{mn} is a divisor {n}")
    else:
        # print(f"{mn} is not a divisor of {n}")
        pass

if mn==0 or mx==0 or n==0:
    raise ZeroDivisionError("Can't except 0 for number-min-max!!\n")
    exit()

else:
    if mn==mx:
        checkdiv()
    else:
        while mn<=mx:
            checkdiv()
            mn += 1
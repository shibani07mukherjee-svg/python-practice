num= int(input("enter a number"))
if num <0 and num % 2 ==0:
    print("NEGATIVE AND EVEN")
elif num <0 and num % 2 !=0:
    print("NEGATIVE AND ODD")
elif num >0 and num % 2 ==0:
    print("POSITIVE AND EVEN")
elif num >0 and num % 2 !=0:
    print("POSITIVE AND ODD")
else:
    print("ZERO")
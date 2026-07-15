marks= int(input("Enter your marks(0-100): "))
if marks <0 or marks> 100:
    print("INVALID MARKS")
elif marks >= 90:
   print("Your Grade is AA")
elif marks >= 80:
    print("Your grade is A")
elif marks >= 70:
    print("Your Grade is B") 
elif marks >= 60:
    print("Your Grade is C")
elif marks >= 50:
    print("Your Grade is D")
else:
    print("YOU ARE FAIL")
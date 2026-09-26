count= 1
even=0
odd=0
num=int(input("enter a number: "))
while count <= num:
    if count % 2 ==0:
        even+=1
    else:
        odd+=1
    count+=1
print("even numbers are: ", even)
print("odd numbers are: ", odd)
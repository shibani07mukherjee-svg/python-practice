username= "shibani"
password= "1234"
chance= 1
while chance <= 3:
    user=input("Enter username : ")
    pwd= input("Enter password : ")
    if user == username and pwd == password:
        print("Login successful")
        break
    else:
        print("login faild. You have", 3-chance, "chance left")
    chance= chance+1
if chance == 4:
    print("Account Locked")
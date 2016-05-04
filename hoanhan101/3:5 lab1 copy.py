from turtle import*
##while True:
##    x = input("What direction? ")
##    if x=="right":
##        right(60)
##        forward(100)
##    elif x=="left":
##        left(60)
##        forward(100)
##    else:
##        break


##while True:
##    x=input("What shape?")
##    if x=="tamgiac":
##        s=3
##    elif x=="vuong":
##        s=4
##    elif x=="ngugiac":
##        s=5
##    else:
##        break
##    for i in range(s):
##        forward(100)
##        left(360/s)
##    


##while True:
##    y = input("Water or not")
##    x = input("What time?")
##    x = int(x)
##    if x=="y":
##        if (x>5 and x<10) or (x>20 or x<22):
##            print("pumping water")
##        else:
##            print("it not time yet")
##    else:
##        print("there is no water")

##while True:
##    x = input("Enter a number: ")
##    x=int(x)
##    if x%2==1:
##        print("This is a odd number")
##    else:
##        print("This is an even number")
##        break
##if x**(1/2)%2==0:
##    print(x,"is a square number")
##else:
##    print(x,"is not a square number")

##while True:
##    x=input("Number = ")
##    x=int(x)
##    a=x**(1/2)
##    a=float(a)
##    if int(a) == float(a):
##        print(a,"is a square number")
##    else:
##        print(a,"is not a square number")

while True:
    x=input("username ")
    if len(x)==0:
        print("You must enter your username")
    else:
        y=input("passcode ")
        if x=="bighero6":
            if y=="codethechange":
                print("Welcome to techkid 2016")
                break
            else:
                print("Wrong passcode")
        else:
            print('Again')

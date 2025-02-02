
def start():
    #while True will create a loop if the user inputs something invalid
    while True:
        CustName= str(input("Please enter your name. "))
        if CustName == "":
            print("Invalid please submit a name.")
            continue
        else:
            break
        
    while True:
        UnitName= str(input("What item are you purchasing " + CustName + "? "))
        if UnitName == "":
            print("Invalid please submit a product name.")
            continue
        else:
            break

    while True:
        #I made the input for this a str input to check for letters later
        UnitQty= input("How many are you buying? ")
        if UnitQty.isalpha() == True: #This checks for any letters
            print("Invalid. Please enter a number.")
            continue
        elif UnitQty.isalpha() != True: #If the input does not have letters it will change to a int
            UnitQty=int(UnitQty)
            #This if statement will check if the input is greater than 0
            if UnitQty <= 0:
                print ("Invalid. Input a number greater than zero.")
                continue
            else:
                break            
        else:
            print("Invalid. Please enter a number.")
            continue
        
    while True:
        PricePer= input("How much does a " + UnitName + " cost per unit? $")
        if PricePer.isalpha() == True : #This checks for any letters
            print("Invalid. Please enter a number.")
            continue
        elif PricePer.isalpha() != True: #Once again if there are no letters then this will change to a float
            PricePer=float(PricePer)
            #This if statement will check if the input is greater than 0
            if PricePer <= 0:
                print ("Invalid. Input a number greater than zero.")
                continue
            else:
                break
        else:
            print("Invalid. Please enter a number.")
            continue
    
    TotalCost= PricePer * UnitQty

    print("The total cost is: $"+ str(round(TotalCost,2)))

    #I made this line to see if the user is purchasing more than one item
    #If true then the code will make the appropriate adjustments
    if UnitQty > 1:
        UnitName = str(UnitName) + "s"
    
    print(CustName + " has purchased " + str(UnitQty) + " " + str(UnitName) + " for " + str
          (round(TotalCost,2)))

    while True:
        CustReset= str(input("Would you like to continue and start over? (y/n)"))
        if (CustReset not in {"y","Y","n","N"}):
            print("Invalid response try again")
            continue
        elif (CustReset in {"y","Y"}):
            start()
        elif (CustReset in {"n","N"}):
            exit()

start ()

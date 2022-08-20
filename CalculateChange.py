#Change Calculator Assignment
#IS280 Summer 2022
#Victoria V. Shearing

#!/usr/bin/env python3

def getCoin(coinType):
    coinCount = -1
    while coinCount < 0:
        try:
            coinCount = int(input("How many " + coinType + " do you have? "))
            if coinCount < 0:
                print("Coin counts cannot be negative. Please re-enter.")
        except ValueError:
            print("Input must be a non-negative integer. Please re-enter.")
    #while loop ends at the line above
    return coinCount

def getUserInput():
    choice = ""
    while choice == "":
        try:
            choice = input("Do you have change (y/n)? ")
            if choice == "":
                print("the answer cannot be empty.  Please try again. ")
        except:
            print()
    return choice
            

runningTotal = 0

print("Welcome to the Change Calculator")
print()
#priming read: input value is obtained before the loop
#and then again inside the loop at the end

#choice = input("Do you have change (y/n)? ")
choice = getUserInput()

while choice[0].lower() == "y":
     #call the getCoin method which returns the input value as an int
    halfDollars = getCoin("half-dollars")
    quarters = getCoin("quarters")
    dimes = getCoin("dimes")
    nickles = getCoin("nickles")
    pennies = getCoin("pennies")
    
    totalValue = halfDollars*50 + quarters*25 + dimes*10 + nickles*5 + pennies
    dollarValue = int(totalValue/100)
    centsValue = totalValue%100
    runningTotal = runningTotal + totalValue
    print()
    print("You have: " + str(totalValue)+ " cents")
    print("Which is "+ str(dollarValue)+ " dollars and " + str(centsValue) + " cents")
    print()    

    choice = input("Do you have more change (y/n) ? ")
    print()

dollars = int(runningTotal/100)
cents = runningTotal % 100

                      
print("Thanks for using the change calculator!")
print("You had a total of " + str(runningTotal) + " cents")
print("which is " + str(dollars) + " dollars and " + str(cents) + " cents.")


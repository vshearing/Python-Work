'''Guessing Game Assignment
   IS280 Summer 2022
   Victoria Shearing'''

''' The game should generate a random integer between 1 and 100 and then let the user try to guess the number,
providing various types of feedback according to how close the guess is to the actual value.'''

import random

#global variables
prevCat = 0
prevDiff = 0

def main():
    print("Welcome to the guessing game!")
    print()

    gametype = getChoice()
    while gametype !=0:
       rnum = random.randint(1, 100)
       print()
       print("I am thinking of a number between 1 and 100.")
       if gametype == 1:
          playHotCold(rnum)
       elif gametype == 2:
           playHighLow(rnum)
       else:
           print("I do not understand game type: " + str(gametype))
           
       gametype = getChoice()
       print()
    #end of while loop
    print("Thank you for playing!")

def getChoice():
    #in final version the program must be robust
    #doesnt crash on illegal input and only return 0, 1, and 2
    goodVal = False
    while not goodVal:
        try:
            choice = int(input("Game Type: 1 = Hot/Cold, 2 = High/Low, 0 = Quit "))
            if choice < 0 or choice > 2:
                print("Unknown operation. Please select from available choices.")
            else: goodVal = True
        except ValueError:
            print("Illegal input, please enter integers between 0 and 2 only.")
    
    return choice
    
def getGuess():
    #must be robust in final version: returns only integers from 1 - 100 or 0
    goodVal = False
    while not goodVal:
        try:
            userGuess = int(input("Your Guess (1 - 100, 0=Quit)? "))
            if userGuess < 0 or userGuess > 100:
                print("Pease enter a number between 1 and 100, or 0 to quit.")
            elif userGuess == 0:
                print("You selected 'quit', thank you for playing!")
                goodVal = True
            else:
                goodVal = True
        except ValueError:
            print("Enter numbers only please!")
    return userGuess


def showHotCold(rnum, guess):
    global prevCat, prevDiff
    category = 0
    diff = abs(rnum - guess)
    #print("Your guess was " + str(diff) + " away from the number. ")
    msg = ""
    if diff >=60:
        category = 1  #cold category
        msg = "cold"
    elif diff >=30:
        category = 2 #warm category
        msg = "warm"
    elif diff >= 16:
        category = 3 #very warm category
        msg = "very warm"
    else:
        category = 4 #hot category
        msg = "hot"
    #print("You are " + msg)
    if category == prevCat:
        #need additional message modifier for warmer, colder, hotter
        if diff == prevDiff:
            msg += " (same degree)"
        elif diff > prevDiff:
            msg += " and getting colder"
        else:
            # modifier message is 'getting warmer' unless they are already hot
            if category == 4:
                msg += " and getting hotter"    
            else:
                msg += " and getting warmer"
    print("Your guess is: " + msg)
    prevCat = category
    prevDiff = diff


def playHotCold(rnum):
    guessCount = 0
    playing = True
    #not a priming read, always ask at least one time for a guess
    #similar to other languages 'do' loops
    while playing:
        guess = getGuess()
        guessCount += 1
        if guess == 0:
            print("Sorry you did not guess my number " + str(rnum) + " in " +
                  str(guessCount - 1) + " tries.")
            playing = False
        elif guess == rnum:
            print("Congratulations!  You guessed my number in " + str(guessCount) +
                  " tries.")
            playing = False
        else:
            #stil playing, did  not guess the number
            showHotCold(rnum, guess) #shows result of guess
            playing = True
    #no return needed at the end of this method


def showHighLow(rnum, guess):
    diff = rnum - guess
    msg = ""
    if diff >0:
        category = 1  #low category
        msg = "too low"
    elif diff < 0:
        category = 2 #high category
        msg = "too high"
    else:
        category = 3 #guessed category
        msg = "correct"
    
    print("Your guess is: " + msg)

        

def playHighLow(rnum):
    guessCount = 0
    playing = True
    #not a priming read, always ask at least one time for a guess
    #similar to other languages 'do' loops
    while playing:
        guess = getGuess()
        guessCount += 1
        if guess == 0:
            print("Sorry you did not guess my number " + str(rnum) + " in " +
                  str(guessCount - 1) + " tries.")
            playing = False
        elif guess == rnum:
            print("Congratulations!  You guessed my number in " + str(guessCount) +
                  " tries.")
            playing = False
        else:
            #stil playing, did  not guess the number
            showHighLow(rnum, guess) #shows result of guess
            playing = True
    #no return needed at the end of this method



if __name__ == "__main__":
    main()


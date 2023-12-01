from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from app import Capital
import random

from io import IOBase


def playGame():
    capital_list = []
    correct = 0

    for capital in Capital.select():
        capital_list.append(model_to_dict(capital))

    print(capital_list)

#need to get integer
    user_input = input("Enter a number: ")

    try:
        # Try to convert the input to an integer
        howmany = int(user_input)
        print("Input is an integer.")
        # Continue your code logic here using the 'number' variable
    except ValueError:
        # If conversion to integer fails, handle the exception
        print("Input is not an integer. Please enter a valid integer.")
        # You might want to prompt the user again for input or take appropriate action
    

        

    again = "n"
    while again == "n":

        rightAns=0
        wrongAns=0

        mylist=capital_list
        random.shuffle(mylist)

        for x in range (0,howmany):
            state_capital=(mylist[x]["capital"])
            state_name = (mylist[x]["name"])
            print ("""Greetings! How well do you know the geography of the United States?
            Guess the capitals of each state and test your knowledge!
            What is the capital of """,state_name )
            guess  = input ("what is your guess?")
            print (guess)
            if guess == state_capital:
                rightAns= rightAns+1
                print("your  score is  ", rightAns , " correct and " ,wrongAns, "   wrong ")
                keepGoing = input ("Press enter to continue") 
                exit
            else:    
                wrongAns=wrongAns+1
                print ("Wrong---answer is  ", state_capital)
                print("your  score is  ", rightAns , " correct and " ,wrongAns, "   wrong ")
                keepGoing = input ("Press enter to continue") 

        


        print("your final score is  ", rightAns , " correct and " ,wrongAns, "   wrong ")
        playItAgain= input ("would you like to play again?  (y or n)")
        print (playItAgain)
        if playItAgain =='n':
            again=="y"
            print ("I had enough")
            print (again)
            #we're done
            exit()
        else:
            print ("Thanks for playing")






def addState():
    print ("add state")
    stateNew=input ("What brilliant state are you creating?")
    capitalNew=input ("What is the capital of your state?")

    Capital.insert({"name": stateNew, "capital": capitalNew}).execute()
    exit()

def needTraining():
    print ("need trainning")
    capital_list = []
    correct = 0

    for capital in Capital.select():
        capital_list.append(model_to_dict(capital))

    print(capital_list)


choice= input ("would you like to play game?  (1) \n Add a bluestate (2) \n need training(3) \n quit (4)?)")
if choice=='1':
    playGame()
elif choice =='2':
    addState()
elif choice=='3':
    needTraining()
else:
    exit()    



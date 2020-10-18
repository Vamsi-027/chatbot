"""
1.Start with a greeting and asks user name
2.Greet user with his/her name
3.Bot displays what it can do[menu] and asks user to choose the operation
4.Responds to user inputs correctly
5.Says GoodBye when programme terminates
"""

import random
from datetime import datetime
from omdb import imdb_bot
from handcricket import hand_cricket
from rockpaperscissor import rock_paper_scissor
from evalexp import eval_exp
from curtime import cur_time
from greetings import greeting_bot


# wishes with respect to time with user name
def welcome(name):
    print(f"{cur_time()} {name}")

# list of things bot can do


def menu():
    print("Things that I can do")
    print("1.Calculate an expression")
    print("2.Get current time")
    print("3.Play Rock-Paper-Scissor")
    print("4.Play Hand Cricket")
    print("5.IMDB bot")
    print("6.End chat")
    print("-------------------")
    try:
        return int(input("Enter your choice[1-6] :"))
    except:
        print("Enter choice from 1,2,3 and 4")


def bot():
    greeting_bot()
    name = input("Enter your name: ")
    welcome(name)
    choice = menu()
    while(choice != 6):
        if(choice == 1):
            eval_exp()
        elif choice == 2:
            print("Current time is:", str(datetime.now()))
        elif choice == 3:
            rock_paper_scissor(name)
        elif choice == 4:
            hand_cricket(name)
        elif choice == 5:
            imdb_bot()
        else:
            print("Please enter a number from 1,2,3,4,5 and 6")
        choice = menu()


bot()

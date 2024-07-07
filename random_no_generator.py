import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess the number or Quit(Q/q): ")
    if(userChoice == "Q" or userChoice == "q"): 
        print("You quit the game....")
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("success -- Correct Guess!! ")
        break
    elif(userChoice < target):
        print("The number was too small.Choose the bigger number....")
    else:
        print("The number was too big.Choose the smaller number")

print("***** Game Over *****")
g = input("Hello please enter your name!: ")
print(g, end= " ")
gameChoice = input("Would You like to play hangman?\n").upper()
while True:

 if gameChoice == "YES" or gameChoice == "Y":
            print("Lets Begin")
            break
 elif gameChoice == "NO" or gameChoice == "N":
            print("Please? Someone needs to play this for me")
            break
 else:
            print("Please Answer only Yes or No")

            break

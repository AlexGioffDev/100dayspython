import random

choice = int(input("What do you choose? 0: Rock, 1: Paper, 2: Scissors. "))

choices = ["Rock", "Paper", "Scissors"]
choice_pc = choices[random.randint(0, len(choices))]

if choice < 0 or choice > 2:
  print("Error Choice")
else:
  print(f"PC Choice: {choice_pc}")
  if choice == 0 and choice_pc == "Rock":
      print("You Draw")
  elif choice == 0 and choice_pc == "Paper":
     print("You lose")
  elif choice == 0 and choice_pc == "Scissors":
     print("You Win")
  elif choice == 1 and choice_pc == "Rock":
      print("You Win")
  elif choice == 1 and choice_pc == "Paper":
     print("You Draw")
  elif choice == 0 and choice_pc == "Scissors":
     print("You Lose")
  elif choice == 2 and choice_pc == "Rock":
      print("You Lose")
  elif choice == 2 and choice_pc == "Paper":
     print("You Win")
  elif choice == 2 and choice_pc == "Scissors":
     print("You Draw")
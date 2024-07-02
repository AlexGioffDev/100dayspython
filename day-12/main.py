import random
from util import clear, logo
game_over = True


def get_guess():
  while True:
    try:
      guess = int(input("Try to guess the number (1-100): "))
      if 1 <= guess <= 100:
        return guess
      print("Please enter a number between 1 and 100")
    except ValueError:
      print("Invalid input. Please enter a valid number.")

def game():
  clear()
  print(logo)
  lives = 10
  level = input("Do you want to play hard mode? write y to say yes:  ")
  if level.lower() == "y":
    lives = 5

  random_number = random.randint(1, 100)
  while lives > 0:
    print(f"Lives remain: {lives}")
    user_guess = get_guess()

    if user_guess == random_number:
      print("You win")
      return
    elif user_guess > random_number:
      print("Too high! ")
      lives -= 1
    else:
      print("Too Low!")
      lives -= 1

  print("You Lose! No more lives!!")


while game_over:
  game()

  again = input("type y to play again other letter to close: ")
  if again.lower() != 'y':
    game_over = False
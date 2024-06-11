import random 
from utility import stages,logo, word_list

gameOver = False
lives = 6
correct = False
aleardy_used: list[str] = []


print(logo)
chosen_word = random.choice(word_list)

dipslay: list[str] = []
for _ in range(len(chosen_word)):
  dipslay.append("_")

while not gameOver:
  correct = False
  guess = input("Guess a letter: ").lower()
  if guess in aleardy_used:
    print("You already try this letter!")
    continue

  aleardy_used.append(guess)
  
  for (i,letter) in enumerate(chosen_word):
    if letter == guess:
      dipslay[i] = letter
      correct = True
  
  if not correct:
    lives -= 1
    if lives < 1:
      print(f"You lose!The correct answer was: {chosen_word}")
      gameOver = True
      break

  for letter in dipslay:
    print(letter, end=" ")
  
  print(stages[lives])

  if "_" not in dipslay:
    gameOver = True
    print("You Win")


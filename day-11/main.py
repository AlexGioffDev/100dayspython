from util import clear, logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_cards(n = 2):
  your_cards = []
  for _ in range(n):
    your_cards.append(random.choice(cards))
  return your_cards


def check_cards(cards):
  total = sum(cards)
  while total > 21 and 11 in cards:
    cards[cards.index(11)] = 1
    total = sum(cards)
  return total



def play():
  clear()
  print(logo)
  player_cards = get_cards()
  pc_cards = get_cards()
  score_user = 0
  score_pc = 0
  print(f"Your cards: {player_cards}")
  print(f"Computer's first card: {pc_cards[0]}")

  while True:
    other_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if other_card.lower() == 'y':
      player_cards.append(random.choice(cards))
      print(f"Your cards: {player_cards}")
      print(f"Computer's first card: {pc_cards[0]}")
      score_user = check_cards(player_cards)
      if score_user > 21:
        print(f"You already looose")
        play_again = input("You want to play again? type y: ")
        if play_again.lower() == 'y':
          play()
        else:
          return

    else:
      break
  print(f"Your final hand: {player_cards}")
  print(f"Computer's final hand: {pc_cards}")
  score_pc = check_cards(pc_cards)
  score_user = check_cards(player_cards)

  print(f"Score User: {score_user}")
  print(f"Score PC: {score_pc}")

  if score_user > 21:
    print("You Loose")
  elif score_user <= 21 and  score_pc < score_user:
    print("You win!")
  else:
    print("The pc win the game!")
    
  play_again = input("You want to play again? type y: ")
  if play_again.lower() == 'y':
    play()


  

play_game = input("Do you want to play blackjack? write y to play: ")
print(play_game)

if play_game.lower() == 'y':
  play()


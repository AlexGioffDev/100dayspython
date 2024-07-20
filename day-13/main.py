from util import logo, vs, clear
from data import data
import random
score = 0

def game():
  global score
  game_on = True
  user_data = random.choice(data)
  other_data = random.choice(data)
  while other_data['name'] == user_data['name']:
    other_data = random.choice(data)
  while game_on:
    clear()
    print(logo)
    if score > 0:
      print(f"You are correct! your score is {score}")
    print(f"Compare A: {user_data['name']}, a {user_data['description']}, from {user_data['country']}")
    print(vs)
    print(f"Against B: {other_data['name']}, a {other_data['description']}, from {other_data['country']}")
    more_follower = input("Who has more followers? type 'A' or 'B': ")
    while more_follower.upper() != "A" and more_follower.upper() != "B":
      more_follower = input("Who has more followers? type 'A' or 'B': ")

    if (more_follower.upper() == 'A' and user_data['follower_count'] > other_data['follower_count']) or (more_follower.upper() == 'B' and other_data['follower_count'] > user_data['follower_count']):
      score += 1
      user_data = other_data
      other_data = random.choice(data)
      while other_data['name'] == user_data['name']:
        other_data = random.choice(data)
    else:
      clear()
      print(logo)
      print(f"You Lose! Your score is: {score}")
      game_on = False
   



game() 
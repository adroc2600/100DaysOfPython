from game_data import data
from art import logo, vs
import random

'''EXAMPLE DATA ENTRY
 'name': 'Instagram',
 'follower_count': 346,
 'description': 'Social media platform',
 'country': 'United States'
'''

def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"



def get_guess():
    while True:
        choice = input("\nWho do you think has more followers? Type A or B: ").lower()
        if choice in ['a', 'b']:
            return choice
        print("Invalid input. Please type 'a' or 'b'.")

def play_again():
    while True:
        choice = input("\nDo you want to play again? Type Y or N: ").lower()
        if choice in ['y', 'n']:
            return choice
        print("Invalid input. Please type 'Y' or 'N'.")

score = 0

print(logo)

while True:
  #works but clunky
  #rand_dataA = random.randint(0, len(data) - 1)
  #rand_dataB = random.randint(0, len(data) - 1)

  # Works better but can produce same result for a and b
  #rand_dataA = random.choice(data)
  #rand_dataB = random.choice(data)
  
  rand_dataA, rand_dataB = random.sample(data, 2)

  print(f"Compare A:  {format_data(rand_dataA)}")
  print(vs)
  print(f"Against B:  {format_data(rand_dataB)}")

  guess = get_guess()

  if guess == 'a' and rand_dataA['follower_count'] > rand_dataB['follower_count']:
    score += 1
    print("\nCorrect, your current score is: ", score)
  else:
    print("\nIncorrect, your final score is:", score)
    again = play_again()
    if again == 'y':
        score = 0
    else:
      break
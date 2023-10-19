from art import logo
from game_data import data
import random

print(logo)
#Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

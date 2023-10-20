from art import logo, vs
from game_data import data
import random
from replit import clear


#Takes the account data and return the printable format
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

#Takes the user guess and follower counts and return if they got it right
def check_answer(guess, a_folowers, b_followers):
    if a_folowers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

     

print(logo)
score = 0
game_should_continue =True
 #Generate a random account from the game data
account_b = random.choice(data)

#Make the game repeatable
while game_should_continue:        
    #Make account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Get follower count of each account   
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count )
    #clear the screen between rounds
    clear() 
    print(logo)
    #Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right {score}")
    else:
        game_should_continue = False
        print(f"Dorry, that's wrong {score}")






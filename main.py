from art import logo
import random
print(logo)
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100 ")
difficulty =input("Choose a dificulty. Type 'easy' or 'hard' : ")
remaining_guesses = None
if difficulty == 'easy':
    remaining_guesses = 10
elif difficulty  == 'hard':
    remaining_guesses = 5
random_number = random.randint(1,100)
print(f"You have {remaining_guesses} attempts remainig to guess the number")

game_over = False
correct_guess = False
def check_guess(guess,random_number):
    global remaining_guesses
    global game_over
    global correct_guess
    if guess > random_number:
        remaining_guesses -= 1
        print('Too high')
        correct_guess = False
    elif guess < random_number:
        remaining_guesses -= 1
        print('Too low')
        correct_guess = False
        
    else:
        print(f"you got it, The answer was {random_number}")
        game_over = True
        correct_guess = True

while not game_over:
    if remaining_guesses > 0:
        guess = int(input("Make a guess : "))
        check_guess(guess,random_number)
        if not correct_guess:
            print("Guess again")
            print(f"You have {remaining_guesses} attempts remainig to guess the number")
    else:
        print("You lost")
        game_over = True
    
    



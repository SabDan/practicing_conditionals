"How many M&Ms are in a jar?"
import random


print('-----------------------')
print("  Guess How Many M&M's     ")
print('-----------------------')

print("Guess the number of M&M's and you get a free lunch.")
print()

mm_count = random.randint(1,100) # number of m&m's
attempt_limit = 7 # given 5 attempts
attempts = 0

while attempts < attempt_limit: # Boolean- True of False. while True
    guess_text = input("How many M&M's are in the jar? ") # code runs as long as the statement is true
    guess = int(guess_text)
    attempts += 1  # counting up the remaining guesses

    if guess == mm_count:
        print(f"You have free lunch! It was {guess} in the jar")
        break
    elif guess < mm_count:
        print("Sorry too LOW")
    else:
        print("Your guess is too HIGH!")


"Choose a Number Game"
guess = None

while guess != 0:
    user_pick_number = int(input("Please choose a number. "))
    if user_pick_number == 0:
        print("Goodbye")
        break
    if (user_pick_number % 2 ) == 0:
        print("Even")
    elif (user_pick_number % 1) == 0:
        print('Odd')

















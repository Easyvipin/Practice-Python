import random # random is a python module used to generate random numbers, and choose a random value from lists, etc.

def start_game(tries):
    """This function takes a `tries` argument. This is the amount of attempts until the game is over"""
    user_tries = 0
    
    random_number = random.randint(0, 10)

    while user_tries < tries:
        user_tries += 1 # Add 1 to the try counter.
      
        guess = int(input("Guess: ")) # Get the user's guess.
      
        if guess == random_number:
            # The user guessed correctly
            print("Correct! The random number was", random_number)
            
            return

        print("Incorrect!")

    print("You did not guess within the correct amount of tries! The number was", random_number)

start_game(10)

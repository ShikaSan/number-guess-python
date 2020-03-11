# Simple guess the random number game

import random # Import this module for generating a random number

secretNumber = random.randint(1, 20) # Set the random number as a global variable

# Function to determine if answer is too low, too high, or if it is correct
def guessFunc(guessInput, randomNum):
    if guessInput < randomNum:
        return 'The number is too low.';
    elif guessInput > randomNum:
        return 'The number is too high.'
    else:
        return 'Correct!'

# The "main" function of the whole game
def mainFunc(randomGen_Number):
    userGuess = ''
    guessResult = ''

    # Game loop, the program ends if user types 'Exit'/'exit' or guesses the correct answer.
    while True:
        print('I\'m thinking of a number between 0 and 20...')
        userGuess = input()
        
        if userGuess=='Exit' or userGuess=='exit':
            return
        else:
            guessResult = guessFunc(int(userGuess), randomGen_Number)
            print(guessResult + '\n')
            
        if guessResult == 'Correct!':
            return

# Initialize/call main function       
mainFunc(secretNumber)

    

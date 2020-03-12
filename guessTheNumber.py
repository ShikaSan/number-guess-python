# Simple guess the random number game

import random # Import this module for generating a random number

# Function to generate a random number
def generateRandom_Num():
    randomNum = random.randint(1, 20)
    return randomNum

# Function to determine if answer is too low, too high, or if it is correct
def guessFunc(guessInput, randomNum):
    if guessInput < randomNum:
        return 'The number is too low'
    elif guessInput > randomNum:
        return 'The number is too high.'
    else:
        return 'Correct!'

# Function that checks if user input is valid.
def checkValid_Input(userInput):
    if userInput.isdigit():
        return True

    return False;

# The "main" function of the whole game
def mainFunc():
    userGuess = ''
    guessResult = ''
    getRandom_Num = generateRandom_Num()

    # Game loop, the program ends if user types 'Exit'/'exit'.
    while True:
        print('I\'m thinking of a number between 0 and 20...')
        userGuess = input()

        # Check first if user typed 'exit'. If true, terminates the program
        # if False, continues code execution.
        if str.lower(userGuess) == 'exit':
            return;
        
        # If the previous condition is false, perform this method.
        # This checks if user input is valid.
        isValid = checkValid_Input(userGuess)
        
        if isValid==False:
            print('Invalid input, please try again.\n')
        else:
            guessResult = guessFunc(int(userGuess), getRandom_Num)
            print(guessResult + '\n')
            
            if guessResult == 'Correct!':
                    return mainFunc()

# Initialize/call main function       
mainFunc()

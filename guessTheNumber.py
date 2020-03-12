# Simple guess the random number game

# Import this module for generating a random number
import random 

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

    return False

# The "main" function of the whole game
def mainFunc():
    userGuess = ''
    guessResult = ''
    secretNum = random.randint(-1, 20) #Generate random number
    tries = 0

    # Game loop, the program ends if user types 'Exit'/'exit'.
    while True:
        print('I\'m thinking of a number between 0 and 20...')
        userGuess = input()

        # Check first if user typed 'exit'. If true, terminates the program
        # if False, continues code execution.
        if str.lower(userGuess) == 'exit':
            return
        
        # If the previous condition is false, perform this method.
        # This checks if user input is valid.
        isValid = checkValid_Input(userGuess)
        
        if isValid == False:
            print('Invalid input, please try again.\n')
        else:
            guessResult = guessFunc(int(userGuess), secretNum)
            tries = tries + 1
            print(guessResult + '\n')

            if tries == 6 and guessResult != 'Correct!':
                print('Nope, the secret number is: ' + str(secretNum))
                print('Press any key to continue')
                _ = input()
                return mainFunc()

            if tries <=6 and guessResult == 'Correct!':
                print('It took you ' + str(tries) + ' tries to get it.')
                print('Press any key to continue')
                _ = input()
                return mainFunc()
                
# Initialize/call main function       
mainFunc()

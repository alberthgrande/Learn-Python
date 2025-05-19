import random

print('Welcome to the Number Guessing Game!')
print('Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)')
level = int(input('Please select a difficulty level: '))

guess_number = random.randint(1, 101)
print(guess_number)


def guess_the_number(chance):
    while chance > 0:
        guess_input = int(input('Guess a number between 1 and 100: '))
        if guess_input == guess_number:
            print('Congrats! You guessed the correct number!')
        else:
            print('Sorry, you guessed the wrong number!')
            print('Guess again!')
            chance = chance - 1
            print(f'Chances:  {chance}')

    print('Game over!')


if level == 1:
    print('Level 1')
    chances = 10
    guess_the_number(chances)

elif level == 2:
    print('Level 2')
    chances = 5
    guess_the_number(chances)

elif level == 3:
    print('Level 3')
    chances = 3
    guess_the_number(chances)


else:
    print('Invalid input!')

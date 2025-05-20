import random
import time


def guess_time(start_time):
    run_time = time.time() - start_time
    hours, remainder = divmod(run_time, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours >= 1:
        return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'
    else:
        return f'{int(minutes):02}:{int(seconds):02}'


try:

    print('Welcome to the Number Guessing Game!')
    print('Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)')
    level = int(input('Please select a difficulty level: '))

    guess_number = random.randint(1, 101)
    print(guess_number)
    start_timer = time.time()


    def guess_the_number(chance):
        number_of_attempts = 0

        while chance > 0:
            try:
                guess_input = int(input('Guess a number between 1 and 100: '))
            except ValueError:
                print('Invalid input! Please enter a valid number.')
                continue

            number_of_attempts += 1

            if guess_input == guess_number:
                print('🎉 Congrats! You guessed the correct number!')
                print('⏱ Time taken:', guess_time(start_timer))
                print('Numbers of attempts:', number_of_attempts)
                return
            else:
                print('❌ Sorry, you guessed the wrong number!')
                chance -= 1
                print(f'🔁 Chances left: {chance}\n')

        print('💀 Game over! The number was:', guess_number)
        print('⏱ Time taken:', guess_time(start_timer))


    if level == 1:
        print('🟢 Easy Mode Selected')
        guess_the_number(10)

    elif level == 2:
        print('🟡 Medium Mode Selected')
        guess_the_number(5)

    elif level == 3:
        print('🔴 Hard Mode Selected')
        guess_the_number(3)

    else:
        print('❗ Invalid input! Please run the game again.')

except KeyboardInterrupt:
    print("\n🛑 Game interrupted by user. Goodbye!")

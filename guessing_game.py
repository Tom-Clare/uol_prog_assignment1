from random import randint


def guessing_game():
    correct = False
    attempts = 0
    target = randint(1, 100)
    while not correct:
        attempts += 1  # increment attempts counter
        new_guess = int(input('New guess: '))
        if new_guess == target:
            # exhaust the while loop
            correct = True
        elif new_guess > target:  # incorrect this time, display message and loop around
            print('That\'s not right,', new_guess, 'is too big')
        else:
            print('That\'s not right,', new_guess, 'is too small')

    print('That’s right! You took', attempts, 'guess(es)')

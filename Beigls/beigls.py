"""Бейглз, (c) Эл Свейгарт al@inventwithpython.com
Дедуктивная логическая игра на угадывания числа по подсказкам.
Код размещен на nostarch.com/big-book-small-python-projects
Один из вариантов этой игры приведен в книге Invent Your Own
Computer Games with Python на nostarch.com/inventwithpython
Теги: короткая, игра, головоломка"""

import random

NUM_DIGITS = 3 # (!) Попробуйте задать эту константу равной 1 или 10
MAX_GUESSES = 10 # (!) Попробуйте задать эту константу равной 1 или 100

def main():
    print('''Bagels, a deduction logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {}-digit number with mo re[eated digits.
Try to guess what it is. Here are some clues:
    Pico    One digit is correct but in the wrong position.
    Fermi   One digit is correct and in the right position
    Bagels  No digit is correct
    
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True: # Основной цикл игры.
        # Переменная, в которой хранится секретное число, которое должен угадать игрок
        secretNum = getSecretNum()
        print('I have thought up a number')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Продолжаем итерацию до получение правильне догадки:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # правильно, выходим из игры
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}'.format(secretNum))

        # Спрашиваем игрока, хочет ли он сыграть еще раз
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
def getSecretNum():
    pass
def getClues(a,b):
    pass
main()
import math
import random

import prompt

from brain_games.cli import welcome_user


def brain_gcd(name):
    print('Find the greatest common divisor of given numbers.')
    correct_answers = 0

    while correct_answers < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        expression = f'{num1} {num2}'
        correct_answer = str(math.gcd(num1, num2))

        print(f'Question: {expression}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # NOQA
            print(f"Let's try again, {name}!")
            break

    if correct_answers == 3:
        print(f"Congratulations, {name}!")


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()

    brain_gcd(name)


if __name__ == '__main__':
    main()

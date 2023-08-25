import random

import prompt

from brain_games.cli import welcome_user


def calculate(expression):
    return str(eval(expression))


def brain_calc(name):
    print('What is the result of the expression?')
    correct_answers = 0

    while correct_answers < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(['+', '-', '*'])
        expression = f'{num1} {operator} {num2}'
        correct_answer = calculate(expression)

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
    name = welcome_user()

    brain_calc(name)


if __name__ == '__main__':
    main()

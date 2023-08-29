import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_game():
    number = random.randint(1, 100)
    expression = number
    correct_answer = 'yes' if is_even(number) else 'no'
    return expression, correct_answer

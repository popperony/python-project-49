import random

QUESTION = 'What is the result of the expression?'


def generate_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    expression = f'{num1} {operator} {num2}'
    correct_answer = str(eval(expression))

    return expression, correct_answer

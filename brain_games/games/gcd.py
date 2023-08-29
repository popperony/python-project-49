import math
import random

QUESTION = 'Find the greatest common divisor of given numbers.'


def generate_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    expression = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return expression, correct_answer

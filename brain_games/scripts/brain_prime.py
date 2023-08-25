import random

import prompt

from brain_games.cli import welcome_user


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def brain_prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers = 0

    while correct_answers < 3:
        question_number = random.randint(1, 100)
        correct_answer = 'yes' if is_prime(question_number) else 'no'

        print("Question:", question_number)
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

    brain_prime(name)


if __name__ == '__main__':
    main()

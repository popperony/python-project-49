import random

import prompt

from brain_games.cli import welcome_user


def generate_progression(length, hidden_index):
    start = random.randint(1, 50)
    step = random.randint(1, 5)
    progression = [start + step * i for i in range(length)]
    progression[hidden_index] = '..'
    return progression, start, step


def brain_progression(name):
    print('What number is missing in the progression?')
    correct_answers = 0

    while correct_answers < 3:
        progression_length = random.randint(5, 10)
        hidden_index = random.randint(0, progression_length - 1)

        progression, start, step = generate_progression(progression_length, hidden_index)  # NOQA
        correct_answer = str(start + step * hidden_index)

        print("Question:", ' '.join(map(str, progression)))
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

    brain_progression(name)


if __name__ == '__main__':
    main()

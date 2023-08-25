import random


def is_even(number):
    return number % 2 == 0


def brain_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no"')
    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ").lower()

        if (user_answer == 'yes' and is_even(number)) or (
                user_answer == 'no' and not is_even(number)):
            print("Correct!")
            correct_answers += 1
        else:
            correct_answer = 'yes' if is_even(number) else 'no'
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # NOQA
            print(f"Let's try again, {name}!")
            break

    if correct_answers == 3:
        print(f"Congratulations, {name}!")
import random


def multiplication_quiz(num_problems=5):
    score = 0
    print("Welcome to the Simple Multiplication Quiz!")
    print(f"\nYou will be given {num_problems} multiplication problems to solve.\n")

    for i in range(1, num_problems + 1):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        print(f"Problem {i}: What is {num1} x {num2}?")
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break

            except ValueError:
                print("Please enter a valid integer.")
        correct_answer = num1 * num2

        if user_answer == correct_answer:

            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.\n")
    print(f"You scored {score} out of {num_problems}.")
    if score == num_problems:
        print("Excellent work!")
    elif score > num_problems // 2:
        print("Well done!")
    else:
        print("Keep practicing!")


multiplication_quiz()

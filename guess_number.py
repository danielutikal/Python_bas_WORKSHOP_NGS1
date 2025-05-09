from random import randint

def guess_number():
    """Get number from user.

    User guessing a number until he guess right

    :guess_n: int number handled, if user gives a wrong type (no int number)
    """
    random_number = randint(1, 100)
    guess = 0
    while True:
        while True:
            try:
                guess_n = int(input("Guess a number: "))
                guess = guess_n
                break
            except ValueError:
                print("It's not a number")

        if guess == random_number:
            print("You win!")
            break
        elif guess > random_number:
            print("Too high!")
        else:
            print("Too low!")
    print(f"{guess} is a correct guess.")


if __name__ == "__main__":
    guess_number()


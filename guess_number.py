from random import randint

draw_number = randint(1, 100)
guess_number = 0

while draw_number > 0:
    try:
        guess_number = int(input("Guess a number: "))

    except ValueError:
        print("It's not a number!")

    if guess_number == draw_number:
        print("You win!")
        break

    elif guess_number < draw_number:
        print("Too small!")
        
    elif guess_number > draw_number:
        print("Too big!")



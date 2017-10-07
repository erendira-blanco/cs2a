guess_number = int(input("I m thinking of a number between 1 and 20, guess it:"))
n = int(1,20)

for i in range (1,6):
    while guess_number != n:
        if guess_number < n:
            print("Too low! Guess again.")
        elif guess_number > n:
            print("Too high! Guess again.\n")
    else:
        print("You guessed it!\n")
    break

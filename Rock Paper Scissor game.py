import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    guess = int(input("Enter your guess: "))
    while guess > 3 or guess < 1:
        print("Enter a valid choice please ☺")
        guess = int(input("Enter your guess: "))

    if guess == 1:
        guess_name = 'Rock'
    elif guess == 2:
        guess_name = 'Paper'
    else:
        guess_name = 'Scissors'
    print(f"Your choice is {guess_name}\n")

    print("Now it's the Computer's Turn....")
    com_guess = random.randint(1, 3)

    if com_guess == 1:
        com_guess_name = 'Rock'
    elif com_guess == 2:
        com_guess_name = 'Paper'
    else:
        com_guess_name = 'Scissors'
    print(f"Computer's choice is {com_guess_name}\n")
    print(f"{guess_name} vs {com_guess_name}")

    if com_guess == guess:
        print('It\'s a Draw', end="")
        result = "DRAW"
    elif (guess == 1 and com_guess == 2) or (guess == 2 and com_guess == 1):
        print('Paper wins =>', end="")
        result = 'Paper'
    elif (guess == 1 and com_guess == 3) or (guess == 3 and com_guess == 1):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (guess == 2 and com_guess == 3) or (guess == 3 and com_guess == 2):
        print('Scissors wins =>', end="")
        result = 'Scissors'

    if result == 'DRAW':
        print("<== It's a tie ==>")
    elif result == guess_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")

    ans = input().lower()
    if ans == 'n':
        print("Thanks for playing")
        break

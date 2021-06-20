from random import choice

choices = ["Rock", "Paper", "Scissor"]


def game():
    print("ROCK!! PAPER!! SCISSOR!!")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")

    player_choice = choices[int(input("Choose:")) - 1]
    computer_choice = choice(choices)
    print("Your choice : {0}\nComputer has chosen : {1}".format(player_choice, computer_choice))

    if player_choice == computer_choice:
        print("It's a draw")
        return

    if player_choice == 'Rock':
        if computer_choice == 'Scissor':
            print("You win!!")
        else:
            print("You lost!!")
    elif player_choice == 'Paper':
        if computer_choice == 'Rock':
            print("You win!!")
        else:
            print("You lost")
    elif player_choice == 'Scissor':
        if computer_choice == 'Paper':
            print("You win!!")
        else:
            print("You lost")


name = input("Player Name:")

print("Hello {}!!".format(name))

while True:
    game()
    play_again = input("Play again?\n(Y)es\n(N)o\n")

    if play_again.lower() == 'n':
        break

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


if __name__ == "__main__":
    print("Welcome to Rock-Paper Scissor")
    menu_choice=int(input("Menu:\n1.New Game\n2.Exit\n"))
    if menu_choice == 1:
        player_name = input("Enter player Name:")
        print("Hello {}. Game starting...".format(player_name))
        while True:
            game()
            play_again = input("Play again?\n(Y)es\n(N)o\n")[0].lower()
            if play_again == 'n':
                break
    else:
        print("Exiting game")

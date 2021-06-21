from random import choice
import json

choices = ["Rock", "Paper", "Scissor"]

def game(played,p1_won,cmp_won):
    played+=1
    print("ROCK!! PAPER!! SCISSOR!!")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    player_choice = choices[int(input("Choose:")) - 1]
    computer_choice = choice(choices)
    print("Your choice : {0}\nComputer has chosen : {1}".format(player_choice, computer_choice))

    if player_choice == computer_choice:
        print("It's a draw")
    else:
        if player_choice == 'Rock':
            if computer_choice == 'Scissor':
                print("You win!!")
                p1_won+=1
            else:
                print("You lost!!")
                cmp_won+=1
        elif player_choice == 'Paper':
            if computer_choice == 'Rock':
                print("You win!!")
                p1_won+=1
            else:
                print("You lost")
                cmp_won+=1
        elif player_choice == 'Scissor':
            if computer_choice == 'Paper':
                print("You win!!")
                p1_won+=1
            else:
                print("You lost")
                cmp_won+=1
    
    return (played,p1_won,cmp_won)

if __name__ == "__main__":
    print("Welcome to Rock-Paper Scissor")
    menu_choice=int(input(
            "Menu:\n" +
                "1.New Game\n" + 
                "2.Exit\n"
        ))
    if menu_choice == 1:                #New Game
        player_name = input("Enter player Name:")
        print("Hello {}. Game starting...".format(player_name))
        played,p1_won,cmp_won = 0, 0, 0
        exit=False
        while True:
            played,p1_won,cmp_won=game(played,p1_won,cmp_won)
            while True:
                game_menu = int(input(
                    "Game Menu:\n" +
                        "1.Show score\n" + 
                        "2.Reset score\n" +
                        "3.Play again\n" +
                        "4.Exit Game\n"
                ))
                if game_menu == 1:      #Show score
                    print("Show score:")
                    print("GAMES PLAYED : {}".format(played))
                    print("P1 : {}".format(p1_won))
                    print("CMP : {}".format(cmp_won))
                    print("DRAW : {}".format((played -(p1_won + cmp_won))))
                elif game_menu == 2:    #Reset score
                    played,p1_won,cmp_won = 0, 0, 0
                    break
                elif game_menu == 3:    #Play again
                    break
                elif game_menu == 4:    #Exit Game
                    exit=True
                    break
            if exit:
                break

        """Save Game"""
        save_game = input("Save Game?\n[Y]es\n[N]o\n")[0].lower()        
        if save_game == 'y':
            file_name = input("Enter the file name:")
            output={
                "name":player_name,
                "game":{
                    "played":played,
                    "won":p1_won,
                    "lost":cmp_won,
                    "draw":played-(p1_won+cmp_won)
                }
            }
            f = open(file_name + ".json", "w")
            f.write(json.dumps(output, indent = 1))
    else:                               #Exit
        print("Exiting game")

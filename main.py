#TicTacToe Logo
#Ask user if they want to play
import random
# import call method from subprocess module
from os import system, name

game_token = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

USER_TOKEN = "X"
COMPUTER_TOKEN = "O"


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def check_winner(token):
    # Check rows
    for row in range(len(game_token)):
        if game_token[row][0] == game_token[row][1] == game_token[row][2] == token:
            return True

    # Check columns
    for column in range(len(game_token)):
        if game_token[0][column] == game_token[1][column] == game_token[2][column] == token:
            return True

    # Check diagonal top left to bottom right
    if game_token[0][0] == game_token[1][1] == game_token[2][2] == token:
        return True

    # Check diagonal bottom left to top right
    if game_token[0][2] == game_token[1][1] == game_token[2][0] == token:
        return True

    return False


def show_game_board():
    clear()
    game_board = (f"{game_token[0][0]} | {game_token[0][1]} | {game_token[0][2]}\n"
                  "---------\n"
                  f"{game_token[1][0]} | {game_token[1][1]} | {game_token[1][2]}\n"
                  "---------\n"
                  f"{game_token[2][0]} | {game_token[2][1]} | {game_token[2][2]}\n")
    print(game_board)


def check_free(row, column):
    if game_token[row][column] == " ":
        return True


def game():
    # Ask user for position of token
    user_row = int(input("In which row do you want to place your token? (1/2/3): ")) - 1
    user_column = int(input("In which column do you want to place your token? (1/2/3): ")) - 1

    # Check if position is free
    if check_free(user_row, user_column):
        game_token[user_row][user_column] = USER_TOKEN
    else:
        print("Sorry, this place is already occupied. Please choose another location.\n")
        game()

    # Show game board to user
    print("You have made your choice: ")
    show_game_board()

    # Place computers token
    continue_search = True
    while continue_search:
        computer_row = random.randint(0, 2)
        computer_column = random.randint(0, 2)

        if check_free(computer_row, computer_column):
            game_token[computer_row][computer_column] = COMPUTER_TOKEN
            continue_search = False

    # Show game board to user
    print("The computer has made a choice: ")
    show_game_board()

    # Check for winner
    if check_winner(USER_TOKEN):
        print("You win.")
    elif check_winner(COMPUTER_TOKEN):
        print("The computer wins.")
    else:
        # Ask for new user position
        game()


game()

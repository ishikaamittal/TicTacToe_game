import sys

board = {"1": "", "2": "", "3": "",
         "4": "", "5": "", "6": "",
         "7": "", "8": "", "9": ""}

player_x = "x"
player_o = "o"
game_on = True


def board_design():
    """Design of board"""
    print("\nWELCOME TO TIC TAC TOE GAME :)\n")
    print(f"{board['1']} | {board['2']} | {board['3']}")
    print("---------")
    print(f"{board['4']} | {board['5']} | {board['6']}")
    print("---------")
    print(f"{board['7']} | {board['8']} | {board['9']}")


def player_input(player):
    """Input of player X"""
    print(f"For player '{player.upper()}'")
    position_input = input("Enter the position (from 1 to 9): ")
    if board[position_input] == "":
        if position_input in board:
            board[position_input] = player
            board_design()


def result(player):
    if board["1"] == board["2"] == board["3"] == player:
        print(f"{player} won!")
        return True
    elif board["1"] == board["5"] == board["9"] == player:
        print(f"{player} won!")
        return True
    elif board["4"] == board["6"] == board["5"] == player:
        print(f"{player} won!")
        return True
    elif board["7"] == board["8"] == board["9"] == player:
        print(f"{player} won!")
        return True
    elif board["1"] == board["4"] == board["7"] == player:
        print(f"{player} won!")
        return True
    elif board["2"] == board["5"] == board["8"] == player:
        print(f"{player} won!")
        return True
    elif board["3"] == board["6"] == board["9"] == player:
        print(f"{player} won!")
        return True
    elif board["3"] == board["5"] == board["7"] == player:
        print(f"{player} won!")
        return True
    elif board["1"] != "" and board["2"] != "" and board["3"] != "" and board["4"] != "" and board["5"] != "" and board[
        "6"] != "" and board["7"] != "" and board["8"] != "" and board["9"] != "":
        print(f"It's a Draw")
        return True


def replay():
    if result(player_x or player_o):
        restart = input("Do you want to restart again (y/n):").lower()
        if restart == "y":
            board.update({}.fromkeys(board, ""))
            game()
        elif restart == "n":
            sys.exit()


def game():
    board_design()
    while game_on:
        player_input( player_x)
        replay()
        player_input(player_o)
        replay()


game()

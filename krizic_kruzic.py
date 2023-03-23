
import os

def display_game_board():
    os.system("cls")
    print()
    print("Krizic - Kruzic")
    print()
    print("Igrac 1 (X) \t Igrac 2 (O)")
    print()
    print()
    print(f"\t {game_board[1]} | {game_board[2]} | {game_board[3]}")
    print("\t---|---|---")
    print(f"\t {game_board[4]} | {game_board[5]} | {game_board[6]}")
    print("\t---|---|---")
    print(f"\t {game_board[7]} | {game_board[8]} | {game_board[9]}")

game_board = [0,1,2,3,4,5,6,7,8,9]
player = 1
player_mark = "X"

game_status = -1
while game_status == -1: 
    display_game_board()
    print()
    print(f"Igrač {player} ({player_mark}) je na potezu.")
    user_choice = int(input("Upisite broj polja koje zelite odigrati: "))
    print(f"Igrač {player} ({player_mark}) je odabrao polje {game_board[user_choice]}.")
    print()

    game_board[user_choice] = player_mark

    if player == 1: 
        player = 2
        player_mark = "O"
    else: 
        player = 1
        player_mark = "X"

    if game_board[1] == game_board[2] == game_board[3]:
        print("Pobjeda")



print("\t*-*-* Tik-Tak-Toe game for two players *-*-*")
board = list(range(1, 10))

# game board generation
def board_generation(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

# user's input
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Chose place " + player_token)
        try:
            player_answer = int(player_answer)
        except:
            print("Error! It is not a number")
        continue
    if player_answer >= 1 and player_answer <= 9:
        if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
        else:
            print("This place already taken")
    else:
        print("Error! Input number from 1 to 9")

# checking of win
def win_check(board):
    win_coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coordinates:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

# main function with game logic
def main(board):
    counter = 0
    win = False
    while not win:
        board_generation(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = win_check(board)
            if tmp:
                print(tmp, "win!")
                win = True
                break
        if counter == 9:
            print("Ended in a draw")
            break
    board_generation(board)
main(board)

input("Press ENTER for exit")
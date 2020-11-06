import itertools


def winner(currentGame):
    def isSame(given_list):
        if given_list.count(given_list[0]) == len(given_list) and given_list[0] != 0:
            return 1
        return 0

    # horizontal Winner
    for row in currentGame:
        if isSame(row):
            print(f"Winner is player {row[0]} horizontally! ")
            return True

    # Vertical Winner
    for col in range(len(currentGame)):
        elem = []
        for row in currentGame:
            elem.append(row[col])
        if isSame(elem):
            print(f"Winner is player {elem[0]} vertically! ")
            return True
    # Diagonal Winner
    diag = []
    for ix in range(len(currentGame)):
        diag.append(currentGame[ix][ix])

    if isSame(diag):
        print(f"Winner is player {diag[0]} diagonally! ")
        return True

    diag = []
    for row, col in enumerate(reversed(range(len(currentGame)))):
        diag.append(currentGame[row][col])

    if isSame(diag):
        print(f"Winner is player {diag[0]} diagonally! ")
        return True

    return False


def gameBorad(game_map, player=0, row=0, column=0, justDisplay=False):
    try:
        if game_map[row][column] != 0:
            print("Watch out for unoccupied spaces!")
            return game_map, False
        print("   " + "  ".join([str(i) for i in range(len(game_map))]))
        if not justDisplay:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("Error: Make sure that you input row or column as 1, 2 or 3! ", e)
        return game_map, False
    except Exception as e:
        print('Something went wrong completely!', e)
        return game_map, False


play = True
players = [1, 2]

while play:
    game_size = int(input("What size of tic tac toe board do you want? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False

    player_choice = itertools.cycle(players)
    game, _ = gameBorad(game, justDisplay=True)
    while not game_won:
        current_player = next(player_choice)
        print(f"Player {current_player} is playing currently.")
        played = False

        while not played:
            row_value = int(input("Enter the row number: "))
            col_value = int(input("Enter the column number: "))
            game, played = gameBorad(
                game, current_player, row_value, col_value)

        if winner(game):
            game_won = True
            repeat = input("Do you want to go for another round?(y,n) ")

            if repeat.lower() == 'y':
                print('Restarting the game for you....')
            elif repeat.lower() == 'n':
                print("Adios Amigo!")
                play = False
            else:
                print("You entered the wrong input! Adios Amigo....")
                play = False

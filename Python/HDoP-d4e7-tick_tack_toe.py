# Tick tack toe - 100 days of python - day 4
# Author: Traian 12-6-24
# TODO: Almost done, fix the winner checking bug
# TODO: Modularize it all

import os

board = [
        [" ","|"," ","|"," ",],
        ["-"," ","-"," ","-",],
        [" ","|"," ","|"," ",],
        ["-"," ","-"," ","-",],
        [" ","|"," ","|"," ",],
        ]

display=[
        ["1","|","2","|","3",],
        ["-"," ","-"," ","-",],
        ["4","|","5","|","6",],
        ["-"," ","-"," ","-",],
        ["7","|","8","|","9",],
        ]

player = ["@","@"]
while player[0] != 'X' or player[0] != 'O':
    print("JOGO DA VELHA!")
    player[0] = input("Escolha X ou O pra jogar:\nDigite sua escolha --> ").upper()
    if player[0] == 'X':
        player[1] = 'O'
        break
    if player[0] == 'O':
        player[1] = 'X'
        break
    os.system('clear')

turn = player[0]
choice = 0
over = False
invalid = False
while choice < 1 or choice > 9:
    for i in range(0, 5):
        for j in range(0, 5):
            print(board[i][j], end="")
        print("")
    print(f"Turno = {turn}")
    print("Escolha uma casa para jogar:")
    for i in range(0, 5):
        for j in range(0, 5):
            print(display[i][j], end="")
        print("")
    choice = int(input("------> "))
    os.system('clear')

    if choice == 1 and display[0][0] == '1':
        board[0][0] = turn
        display[0][0] = '#'
    elif choice == 2 and display[0][2] == '2':
        board[0][2] = turn
        display[0][2] = '#'
    elif choice == 3 and display[0][4] == '3':
        board[0][4] = turn
        display[0][4] = '#'
    elif choice == 4 and display[2][0] == '4':
        board[2][0] = turn
        display[2][0] = '#'
    elif choice == 5 and display[2][2] == '5':
        board[2][2] = turn
        display[2][2] = '#'
    elif choice == 6 and display[2][4] == '6':
        board[2][4] = turn
        display[2][4] = '#'
    elif choice == 7 and display[4][0] == '7':
        board[4][0] = turn
        display[4][0] = '#'
    elif choice == 8 and display[4][2] == '8':
        board[4][2] = turn
        display[4][2] = '#'
    elif choice == 9 and display[4][4] == '9':
        board[4][4] = turn
        display[4][4] = '#'
    else:
        print("OPCAO INVALIDA!")
        invalid = True
    
    if invalid != True and turn == player[0]:
        turn = player[1]
    elif invalid != True and turn == player[1]:
        turn = player[0]
    invalid = False

    if board[2][2] != ' ':
        if board[2][2] == board[0][0] and board[2][2] == board[4][4]:
            print(f"{board[2][2]} WON!")
            over = True
        elif board[2][2] == board[0][4] and board[2][2] == board[4][0]:
            print(f"{board[2][2]} WON!")
            over = True
        elif board[2][2] == board[2][0] and board[2][2] == board[2][4]:
            print(f"{board[2][2]} WON!")
            over = True
        elif board[2][2] == board[0][2] and board[2][2] == board[4][2]:
            print(f"{board[2][2]} WON!")
            over = True
    elif board[0][0] != ' ':
        if board[0][0] == board[0][2] and board[0][0] == board[0][4]:
            print(f"{board[0][0]} WON!")
            over = True
        elif board[0][0] == board[2][0] and board[0][0] == board[4][0]:
            print(f"{board[0][0]} WON!")
            over = True
    elif board[4][4] != ' ':
        if board[4][4] == board[4][2] and board[4][4] == board[4][0]:
            print(f"{board[4][4]} WON!")
            over = True
        elif board[4][4] == board[2][4] and board[4][4] == board[0][4]:
            print(f"{board[4][4]} WON!")
            over = True

    
    if over == True:
        for i in range(0, 5):
            for j in range(0, 5):
                print(board[i][j], end="")
            print("")
        break
    choice = 0

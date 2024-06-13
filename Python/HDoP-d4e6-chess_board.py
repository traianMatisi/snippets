# Chess board (not game) - 100 days of python day 4
# Author: Traian 12-6-24

map =   [
        [" ","#"," ","#"," ","#"," ","#",],
        ["#"," ","#"," ","#"," ","#"," ",],
        [" ","#"," ","#"," ","#"," ","#",],
        ["#"," ","#"," ","#"," ","#"," ",],
        [" ","#"," ","#"," ","#"," ","#",],
        ["#"," ","#"," ","#"," ","#"," ",],
        [" ","#"," ","#"," ","#"," ","#",],
        ["#"," ","#"," ","#"," ","#"," ",],
        ]

spot = input("Mark the chess board coordinate: ").lower()


letter = int(ord(spot[0])) - 97 # converting char ascii to integer with ord() and subtracting
number = int(spot[1]) * (-1) # using negative index instead of subtracting one for normal index

map[number][letter] = 'X' # evaluating indexes in custom order letter-->number

for i in range(0, 8):
    for j in range(0, 8):
        print(map[i][j], end=" ")  # normal evaluation of indexes
    print("")

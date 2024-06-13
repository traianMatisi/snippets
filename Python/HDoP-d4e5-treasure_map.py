# Treasure map - 100 days of python day 4
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

spot = input("Mark the treasure spot by numeric coordinates (matrix indexes): ")

i = int(spot[0]) -1
j = int(spot[1]) -1

map[i][j] = 'X'

for i in range(0, 8):
    for j in range(0, 8):
        print(map[i][j], end=" ")
    print("")

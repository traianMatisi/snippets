alphabet =  [
            [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]],
            [
            ["J", "K", "L"],
            ["M", "N", "O"],
            ["P", "Q", "R"]],
            [
            ["S", "T", "U"],
            ["V", "W", "X"],
            ["Y", "Z", "0"]]
            ]

for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            print(i, j, k, alphabet[i][j][k], end=" => ")

print("")

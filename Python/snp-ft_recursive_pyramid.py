def main():
    while True:
        n = int(input('Type a whole positive number: '))
        if n > 0:
            break
    print(mario(n))

def mario(c):
    row = ''
    if c == 1:
        return '#'
    else:
        for i in range(c):
            row += '#'
        print(mario(c-1))
    return row
    
main()

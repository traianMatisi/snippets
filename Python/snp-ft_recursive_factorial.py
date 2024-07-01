def main():
    while True:
        natural_n = int(input('Type a whole positive number: '))
        if natural_n >= 0:
            break
    print(factorial(natural_n))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
main()

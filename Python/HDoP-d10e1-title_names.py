# Name titleing - 100 days of python - day 10
# Author: Traian -26-6-24

def main():
    full_name = input('Type your full name: ').strip().split()
    f_name = full_name[0]
    l_name = full_name[-1]
    titled_name = char_title(f_name, l_name)
    print(titled_name)

def char_title(f_name, l_name):
    return f'{l_name.title()}\' {f_name.title()}' # returning a f-string

main()

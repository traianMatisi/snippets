# Daus in given month - 100 days of python - day 10
# Author: Traian -26-6-24

def main():
    months = { # TODO: Tret number month input
        31:['January', 'March', 'May', 'july', 'August', 'October', 'December'],
        30:['April', 'June', 'September', 'november'],
        28:['February']
    }
    month = input('Which month? ').strip().title()
    year = int(input('Which year? '))
    if is_leap(year):
        months.pop(28)
        months[29] = 'February'
    for k, v in months.items():
        if month in v:
            print(k)

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

main()

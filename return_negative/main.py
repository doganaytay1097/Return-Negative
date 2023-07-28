def make_negative(number):
    if number >= 0:
        return 0 - number
    else:
        return number


numbers = int(input('GIVE A NUMBER: '))

print(make_negative(numbers))

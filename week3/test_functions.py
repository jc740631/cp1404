def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32.0

def square(number):
    """Square the number."""
    return number **2
def main():
    f_degree = celsius_to_fahrenheit(21)
    print(f'{f_degree:.1f}')
    number = 5
    print(f'{number}^2= {square(number)}')


def main():
    f_degree = celsius_to_fahrenheit(21)
    print(f'{f_degree: .1f}')
    print(number, "^2=", square(number))

# start the program

if __name__ == '__main__':
    main()

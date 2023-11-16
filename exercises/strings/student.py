def greet(name):
    return f"Hello, {name}!"

def format_position(x, y):
    return f'({x:.3f}, {y:.3f})'

def interactive_greet():
    naam = input("What is your name? ")
    print(greet(naam))

def tip_calculator():
    input_str = int(input('Enter total price: '))
    percentage = input('Enter tip percentage (default=20): ')

    if percentage == '':
        percentage = 20
    else:
        percentage = int(percentage)

    print(f'You have to pay {input_str + (input_str * percentage / 100)}')

def mask(password):
    return "*" * len(password)

def underline(password):
    return password + "\n" + "-" * len(password)

def box(string):
    top = "+" + "-" * (len(string) + 2) + "+"
    middle = "| " + string + " |"
    bottom = top
    return f"{top}\n{middle}\n{bottom}"

def last_character(string):
    if len(string) != 0:
        return string[len(string) - 1]
    else:
        return None
    
def is_student_id(string):
    if len(string) != 8:
        return False
    
    if string[0] not in 'RSrs':
        return False

    for i in range(1, len(string)):
        if string[i] not in '0123456789':
            return False
        
    return True

def parse_day(string):
    return int(string[:2])


def parse_month(string):
    return int(string[3:5])


def parse_year(string):
    return int(string[6:])

def fix_date(string):
    month = string[:2]
    day = string[3:5]
    year = string[6:]
    return f'{year}/{month}/{day}'

def palindrome(string):
    return string == string[::-1]

def is_capitalized(string):

    if len(string) == 0:
        return False
    
    return string[0].upper() == string[0] and string[1:].lower() == string[1:]

def parse_position_x(string):
    position = string[1:-1]
    comma_point = position.find(',')
    return float(position[:comma_point])

def parse_position_y(string):
    position = string[1:-1]
    comma_point = position.find(',')
    return float(position[comma_point+2:])


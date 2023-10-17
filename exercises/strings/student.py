def greet(name):
    return f"Hello, {name}!"

def format_position(x, y):
    return f'({x:.3f}, {y:.3f})'

def interactive_greet():
    naam = input("What is your name? ")
    print(greet(naam))

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
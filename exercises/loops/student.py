def print_numbers(start, stop, step):
    current = start
    while current < stop:
        print(current)
        current += step

def thanos(queue_size, target_size):
    i = 0
    while queue_size > target_size:
        queue_size //= 2
        i += 1
    return i

def sum_input():
    inp = int(input("Enter integer: "))
    sum = 0
    while inp != 0:
        sum += inp
        inp = int(input("Enter integer: "))
    print(f'The sum equals {sum}')

def factorial(n):
    factor = 1
    for i in range(2, n+1):
        factor *= i
    return factor

def rpg2(n_sides, goal):
    som = 0
    count = 0
    for i in range(1, n_sides+1):
        for j in range(1, n_sides+1):
            som = i+j
            if som >= goal:
                count += 1
    return count / n_sides**2 * 100

def rpg3(n_sides, goal):
    som = 0
    count = 0
    for i in range(1, n_sides+1):
        for j in range(1, n_sides+1):
            for k in range(1, n_sides+1):
                som = i + j + k
                if som >= goal:
                    count +=1
    return count / n_sides**3 * 100

def invest(amount, rate, goal):
    kapitaal = amount
    jaar = 0
    while kapitaal < goal:
        kapitaal += kapitaal * rate / 100
        jaar += 1
    return jaar

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return n > 1

def gcd(x, y):
    for i in range(min(abs(x), abs(y)), 0, -1):
        if x % i == 0 and y % i == 0:
            return i
        
def valid_parentheses(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

def remove_backspaces(string):
    result = ''
    for char in string:
        if char == '\b':
            result = result[:-1]
        else:
            result += char
    return result
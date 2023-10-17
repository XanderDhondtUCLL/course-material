from math import ceil

def total_cost(amount):
    price = amount
    if price < 100:
        price += 10
    if price >= 200:
        price *= 0.95
    return price

def my_abs(x):
    if x < 0:
        x = -x
    return x

def sign(x):
    state = 0
    if x > 0:
        state = 1
    elif x == 0:
        state = 0
    else:
        state = -1
    return state

def rock_paper_scissors(player1_choice, player2_choice):
    rock = 0
    paper = 1
    scissors = 2
    Result = 2
    if player1_choice == player2_choice:
        Result = 0
    elif player1_choice == rock and player2_choice == scissors:
        Result = 1
    elif player1_choice == paper and player2_choice == rock:
        Result = 1
    elif player1_choice == scissors and player2_choice == paper:
        Result = 1
    return Result


def player_movement(position, left_arrow, right_arrow, shift):
    newpos = position
    if shift:
        if left_arrow:
            newpos -= 2
        if right_arrow:
            newpos += 2
    else:
        if left_arrow:
            newpos -= 1
        if right_arrow:
            newpos += 1
    return newpos

def movie_ticket(duration, imax, student, ticket_count):
    if duration <= 90:
        price = 10
    elif duration <= 120:
        price = 11
    elif duration <= 150:
        price = 12
    else:
        price = 15
    if imax:
        price = ceil(price*1.2)
    if student:
        price -= 3
    return price * ticket_count
from math import *


def five():
    return 5

def triple(x):
    return x*3

def average(x,y):
    average = (x+y)/2
    return average

def distance(x1,y1,x2,y2):
    distance = sqrt((x2-x1)**2 +(y2-y1)**2)
    return distance

def buses_needed(people_count,bus_capacity):
    bus_count = people_count/bus_capacity
    return bus_count

def pizza(n_people, slices_per_pizza):
    return ceil(n_people/slices_per_pizza)

def cake(eggs):
    cake_amount = eggs//5
    return cake_amount

def candy_per_child(candy_count,child_count):
    candy = candy_count//child_count
    return candy

def cake2(eggs, flour):
    return min(eggs//5, flour//250)

def cake3(eggs, flour, butter, sugar):
    Eggs = eggs//5
    Flour = flour//250
    Butter = butter//200
    Sugar = sugar//250
    return min(Eggs, Flour, Butter, Sugar)

def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    Eggs = eggs//eggs_per_cake
    Flour = flour//flour_per_cake
    Butter = butter//butter_per_cake
    Sugar = sugar//sugar_per_cake
    return min(Eggs, Flour, Butter, Sugar)


def hours(duration):
    uren = duration//3600
    return uren

def minutes(duration):
    h = hours(duration)
    duration -= 3600 * h
    return duration//60

def seconds(duration):
    m = minutes(duration)
    h = hours(duration)
    duration -= 3600 * h
    duration -= 60 * m
    return duration

def coins(amount):
    five_coins = amount//5
    amount -= 5 * five_coins

    two_coins = amount//2
    amount -= 2 * two_coins

    totaal = five_coins + two_coins + amount
    return totaal
    
def leftover_candy(candy_count, child_count):
    return (candy_count % child_count)

def internet_costs(duration_in_seconds, cost_per_block):
    time = ceil(duration_in_seconds/360)
    return time * cost_per_block

def middle(a, b, c):
    max_ = max(a,b,c)
    min_ = min(a,b,c)
    totaal = a + b + c
    middel = totaal - max_ - min_
    return middel


def last_digit(n):
    return (n%10)

def drop_last_digit(n):
    div10 = n/10
    drop = div10 - ((n%10)/10)
    return round(drop)

def next_player(player, player_count):
    return (player + 1) % player_count

def next_player2(player, player_count):
    return player%player_count + 1

print(next_player(0, 10))
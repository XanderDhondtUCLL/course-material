def split_name(full_name):
    slicednr = 0

    for i in range(len(full_name)):
        if full_name[i] == ' ':
            slicednr = i
    
    voornaam = full_name[slice(0, slicednr)]
    achternaam = full_name[slice(slicednr+1, len(full_name))]
    return(voornaam, achternaam)

def all_equal(xs):
    state = True
    for i in range(1, len(xs)):
        if xs[i-1] != xs[i]:
            state = False
    return state

def all_different(xs):
    state = True
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                state = False
    return state

def increasing(ns):
    state = True
    for i in range(1, len(ns)):
        if ns[i-1] > ns[i]:
            state = False
    return state

def subtuple(xs, ys):
    for i in range(len(xs)-len(ys)+1):
        if xs[i:i+len(ys)] == ys:
            return True
    return False

def passing_percentage(grades):
    percentage = 0.0
    count = 0
    itotal = 0
    for i in grades:
        if i >= 10:
            count += 1
        itotal += 1
            
    percentage = (count/itotal) * 100
    return percentage

def heatwave(temperatures):
    above25 = 0
    above30 = 0

    for i in temperatures:
        if 25 <= i:
            above25 += 1
        if i >= 30:
            above30 += 1

        if above30 < 3 and above25 < 5:
            if i < 25:
                above30 = 0
                above25 = 0
        print(above25)
        print(above30)

    return (above25 >= 5 and above30 >= 3)

def add_points(p1, p2):
    p1x = p1[0]
    p1y = p1[1]
    p2x = p2[0]
    p2y = p2[1]

    p3x = p1x + p2x
    p3y = p1y + p2y
    return (p3x, p3y)

def increase_version(version, breaking_change, new_features):
    x, y, z = version
    if breaking_change:
        return (x + 1, 0, 0)
    elif new_features:
        return (x, y + 1, 0)
    else:
        return (x, y, z + 1)
    
def is_more_recent(v1, v2):
    a, b, c = v1
    x, y, z = v2
    return a > x or (a == x and b > y) or (a == x and b == y and c > z)

def is_older(v1, v2):
    return is_more_recent(v2, v1)

def average(ns):
    return sum(ns)/len(ns)

def empty_seats(used_seats):
    total = 0
    for i in range(1, len(used_seats)):
        if (used_seats[i] - used_seats[i-1]) > 1:
            total += used_seats[i] - used_seats[i-1] - 1

    return total

def split_in_two(xs):
    mid = len(xs) // 2
    left_half = xs[:mid + len(xs) % 2]
    right_half = xs[mid + len(xs) % 2:]
    return (left_half, right_half)

def election_winner(votes):
    if len(votes) == 0:
        return None
    else:
        return max(sorted(votes))

def domino_chain(dominos):
    for i in range(1, len(dominos)):
        _, end = dominos[i-1]
        start, _ = dominos[i]
        if start != end:
            return False
    return True

print(domino_chain(((2, 4), (4, 3), (3, 0), (0, 0), (0, 5), (5, 4))))
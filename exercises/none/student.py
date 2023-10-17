def multiple_choice(right_answer, given_answer):
    total = 0
    if given_answer != None:
        if right_answer == given_answer:
            total += 1
        else:
            total -= 0.2
    else:
        total = 0
    return total

def product(a, b, c):
    if a == None:
        a = 1
    if b == None:
        b = 1
    if c == None:
        c = 1
    return a * b * c 

def multiple_choice(right_answer, given_answer):
    if right_answer == given_answer:
        return 1
    elif given_answer is None:
        return 0
    else:
        return -0.2


def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    n_skipped = 0
    n_taken = 0
    total = 0

    if grade1 is None:
        n_skipped += 1
    else:
        n_taken += 1
        total += grade1

    if grade2 is None:
        n_skipped += 1
    else:
        n_taken += 1
        total += grade2

    if grade3 is None:
        n_skipped += 1
    else:
        n_taken += 1
        total += grade3

    if grade4 is None:
        n_skipped += 1
    else:
        n_taken += 1
        total += grade4

    if grade5 is None:
        n_skipped += 1
    else:
        n_taken += 1
        total += grade5

    if n_skipped > 1:
        return False
    if total / n_taken < 12:
        return False

    return True


def val_grade(grade):
    wtf = grade
    if grade == None:
        wtf = 0
    return wtf
    
def val_skip(List):
    skipcount = 0
    for i in range(len(List)):
        if List[i] == None:
            skipcount += 1
        if skipcount > 1:
            return False
    return True
    
def goe_entrance_exam(grade1, grade2, grade3, grade4, grade5):
    mylist = [grade1]+[grade2]+[grade3]+[grade4]+[grade5]
    count = 0
    average = 0

    if val_skip(mylist):
        for i in range(len(mylist)):
            count += val_grade(mylist[i])
        average = count/len(mylist)
    return average >= 12


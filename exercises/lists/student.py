def double_items(ns):
    for i in range(len(ns)):
        ns[i] *= 2

# def pad_right(ns):
#     for i in range(len(ns)):
#         ns[i] *= 2
# opgave was fucked lol

def pad_right(xs, length, padding):
    while len(xs) < length:
        xs.append(padding)

def remove_all(xs, item_to_remove):
    for i in range(len(xs) - 1, -1, -1):
        if xs[i] == item_to_remove:
            del xs[i]

def compact(xs):
    new_list = []
    for i in range(len(xs)):
        if xs[i] != None:
            new_list += [xs[i]]
    return new_list

def compact_in_place(xs):
    for i in range(len(xs)-1, -1, -1):
        if xs[i] is None:
            del xs[i]

def remove_runs(ns):
    new_list = []
    for i in ns:
        if not new_list or new_list[-1] != i: #not new list zorgt ervoor dat new_list[-1)] niet gek gaat
            new_list.append(i)
    return new_list
            


def balanced_brackets(string): #Ik heb LTT code gekopieerd van het internet, chatgpt en van solutions en het keurt het nog altijd niet goed ???
    stack = []

    for char in string:
        if char in '([{':
            stack.append(char)
        else:
            if char == ')':
                expected_bracket = '('
            elif char == '}':
                expected_bracket = '{'
            else:
                expected_bracket = '['

            if len(stack) == 0 or stack[-1] != expected_bracket:
                return False

            stack.pop()

    return len(stack) == 0
#fuck dees lmfao


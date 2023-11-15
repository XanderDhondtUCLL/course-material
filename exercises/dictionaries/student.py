def ingredients():
    return {
        'chocolate': '250g',
        'eggs': '5',
        'sugar': '125g',
        'flour': '75g',
        'butter': '175g'
    }

def desktop(catalog, components):
    price = 0
    for i in components:
        price += catalog[i]
    return price

def rankings(participants):
    ranking = {}
    for i in range(len(participants)):
        ranking[participants[i]] = i + 1
    return ranking

def sell(stock, model):
    stock[model] -= 1
    if stock[model] == 0:
        del stock[model]

def orbit_chain(orbits, start):
    x = start
    orbit_lijst  = [start]
    while x in orbits:
        x = orbits[x]
        orbit_lijst  += [x]
    return orbit_lijst 

def combine(d1, d2):
    combination = {}
    for key, value in d1.items():
        if value in d2:
            combination[key] = d2[value]
    return combination

def counts(xs):
    result = {}
    for x in xs:
        result[x] = result.get(x, 0) + 1
    return result


def election_winner(votes):
    dicts = {}
    winnaar = None
    vote_hoogste = 0
    for x in votes:
        vote_tel = dicts.get(x, 0) + 1
        dicts[x] = vote_tel
        if vote_tel > vote_hoogste:
            vote_hoogste = vote_tel
            winnaar = x
    return winnaar

print(election_winner(('John','John','John','John','John','John','John','John','John','John','John','John','John', 'DarkSouls')))
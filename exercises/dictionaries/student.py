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

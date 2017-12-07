
# Given 3 int values, a b c, return their sum. 
# However, if one of the values is the 
# same as another of the values, it does not 
# count towards the sum.

# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(x, y, z):

    soma = []
    elementos = [a]
    for valor in elementos:
        if valor in elementos:
            soma.remove(valor)
        else:
            soma.append(valor)
    return sum(soma)


assert lone_sum(1, 2, 3) == 6
assert lone_sum(3, 2, 3) == 2
assert lone_sum(3, 3, 3) == 0

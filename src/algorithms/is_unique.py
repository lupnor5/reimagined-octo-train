"""
Dado un metodo que recibe una cadena, comprobar si todos los caracteres
son unicos o no. 
isUnique("abcde") => True
isUnique("abcded") => fase
"""


# This is the optimal solution with complexity O(n)
def is_unique(s):
    if len(s) > 128:  # complexity 0(1)
        return False
    aux = {}
    i = 0
    for char in s:
        if char in aux:
            return False
        else:
            aux[char] = i
            i += 1
    return True

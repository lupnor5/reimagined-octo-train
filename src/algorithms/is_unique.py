"""
Dado un metodo que recibe una cadena, comprobar si todos los caracteres
son unicos o no. 
isUnique("abcde") => True
isUnique("abcded") => fase
"""

#Esta es una solucion optima con complejidad 0(n)

def is_unique(string):
    if len(string) > 128: #complejidad 0(1)
       return False
    aux = {}
    i=0
    for chr in string: 
     if chr in aux: 
        return False
     else:
        aux[chr]=i
        i+=1
    return True

        


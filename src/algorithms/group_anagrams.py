"""
Un anagrama es una palabra creada a partir de la reordenacion de las letras de otra palabra
Dado un array de strings, devuelve los anagramas agrupados. Cualquier orden es valido

Ejemplo: 
    Input: words = ["saco", "arresto", "programa", "rastreo", "caso"]
    Output: [["saco", "caso"], ["arresto"], ["rastreo"], ["programa"]]    
"""
def group_anagrams(words):
    word_map = {}
    for word in words:
        word_hash=get_word_hash(word)
        if word_hash in word_map:
            word_map[word_hash].append(word)
        else:
            word_map[word_hash] = [word]
    return list(word_map.values())
        
def get_word_hash(word): 
    word_hash = [0] * 26
    for chr in word: 
        index = ord(chr)-ord('a')
        word_hash[index]+=1
    return "".join(map(str, word_hash))


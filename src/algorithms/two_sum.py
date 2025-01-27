"""
Dado un array de numeros enteros y un target, retorna los indices 
de dos numeros para los que la suma sea igual al target.
Puedes asumir que solamente una solucion

Ejemplo 1: 
    Input: nums = [9, 2, 5, 6], target = 7
    Output = [1, 2]
Ejemplo 2:
    Input = nums = [9, 2, 5, 6], target = 100
    Output = None   
"""

def two_sum(nums, target): 
    result = []
    aux = {}
    for i in range(0, len(nums)):
        if nums[i] in aux:
            result.append(aux[nums[i]])
            result.append(i)
            return result
        else: 
            aux[target-nums[i]] = i
    return None
        
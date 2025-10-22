# Conclua a solução para que ela classifique o array de números passado. 
# Se a função passar um array vazio ou um valor nulo/nulo, 
# ela deverá retornar um array vazio.
# Por exemplo:
# solution([1,2,3,10,5]) # should return [1,2,3,5,10]
# solution(None) # should return []

def solutions(nums):
    nums_sorted = map(int, nums)

    nums_ordered = sorted(nums_sorted)

    return nums_ordered

print(solutions([1,2,3,10,5]))
print(solutions([20,2,10]))
print(solutions([2,20,10]))
print(solutions([]))

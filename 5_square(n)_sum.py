# Complete a função de soma quadrada para que ela eleve ao quadrado cada número passado a ela 
# e então some os resultados.
# Por exemplo, para [1, 2, 2] ele deveria retornar 9 porque 1² + 2² + 2² = 9.

def square_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number ** 2
    return sum
    
print(square_sum([2,2,2]))
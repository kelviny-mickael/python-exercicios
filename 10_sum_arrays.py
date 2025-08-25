# Escreva uma função que receba um array de números e retorne a soma deles. 
# Os números podem ser negativos ou não inteiros. Se o array não contiver nenhum número, 
# você deverá retornar 0.
# Exemplos.
# Entrada: [1, 5.2, 4, 0, -1].
# Saída:9.2.
# Entrada: [].
# Saída:0.
# Entrada: [-2.398].
# Saída:-2.398.

def sum_array(numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    
    return sum if len(numbers) > 0 else 0


print(sum_array([10, 20, 30, 40, 50]))
print(sum_array([-1.2, 10, 20, 30, 4.0, -50]))
print(sum_array([]))
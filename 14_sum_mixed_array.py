# Dado um array de inteiros como strings e números, retorne a soma dos 
# valores do array como se todos fossem números.
# Retorne sua resposta como um número.

def sum_mix(arr):
    sum = 0
    for number in arr:
        convert_to_int = int(number)
        sum += convert_to_int

    return sum

sum_mix([10, 20, '30', '40', 50])
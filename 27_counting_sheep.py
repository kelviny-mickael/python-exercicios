# Considere um array/lista de ovelhas onde algumas ovelhas 
# podem estar faltando em seus lugares. Precisamos de uma função 
# que conte o número de ovelhas presentes no array (true significa presente).
# Por exemplo:
# [True,  True,  True,  False,
#  True,  True,  True,  True ,
# True,  False, True,  False,
# True,  False, False, True ,
# True,  True,  True,  True ,
# False, False, True,  True]
# A resposta correta seria 17.
# Dica: Não se esqueça de verificar se há valores ruins como null/undefined.
def count_sheeps(sheep):
    
    count_true_sheep = []

    for count_sheep in sheep:
        if count_sheep == True:
            count_true_sheep.append(count_sheep)

    return len(count_true_sheep)

count_sheeps([True, True, True, False,
              True, True, True, True,
              True, False, True, False,
              True, False, False, True,
              True, True, True, True,
              False, False, True, True])
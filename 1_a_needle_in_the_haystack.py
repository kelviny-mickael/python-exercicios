# Você consegue encontrar a agulha no palheiro?
# Escreva uma função findNeedle()que receba um arraymonte de lixo, 
# mas que contenha um "needle".
# Depois que sua função encontrar a agulha, ela deverá retornar uma 
# mensagem (como uma string) que diz:
# "found the needle at position "mais indexele encontrou a agulha, então:
# Exemplo (Entrada --> Saída)
# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at 
# position 5".

def find_needle(haystack):
    position = haystack.index('needle')
    return f'Found the needle at position {position}'

found_result = find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])

print(found_result)
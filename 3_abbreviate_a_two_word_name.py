# Escreva uma função para converter um nome em iniciais. 
# Este kata aceita, estritamente, duas palavras com um espaço entre elas.
# A saída deve ser duas letras maiúsculas com um ponto separando-as.
# Deve ficar assim:
# Sam Harris=>S.H.
# patrick feeney=>P.F.

def abbrev_name(name):
    first_letter = name[0]
    position_second_letter = name.find(' ')
    second_letter = name[position_second_letter + 1]
    
    result = first_letter.upper() + '.' + second_letter.upper()

    return result

print(abbrev_name('kelviny mickael'))
print(abbrev_name('maria clara'))
print(abbrev_name('pedro lucas'))
print(abbrev_name('leticia silva'))

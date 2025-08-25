# Crie uma função que responda à pergunta "Você está tocando banjo?".
# Se o seu nome começar com a letra "R" ou com "r" minúsculo, você está tocando banjo!
# A função recebe um nome como seu único argumento e retorna uma das seguintes strings:
# name + " plays banjo".
# name + " does not play banjo".
# Os nomes fornecidos são sempre strings válidas.

def are_you_playing_banjo(name):
    name_banjo = name[0]

    print(name_banjo)

    if name_banjo == 'R' or name_banjo == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

print(are_you_playing_banjo('martin'))
print(are_you_playing_banjo('Rikke'))
print(are_you_playing_banjo('bravo'))
print(are_you_playing_banjo('rolf'))
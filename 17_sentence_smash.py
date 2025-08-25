# Escreva uma função que receba um array de palavras e as junte em uma frase, retornando-a.
# Você pode ignorar a necessidade de sanitizar palavras ou adicionar pontuação, 
# mas deve adicionar espaços entre cada palavra.
# Cuidado, não deve haver espaço no início ou no final da frase!
# Exemplo:
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

def smash(words):
    phrase = ''
    for word in words:
        phrase += word + ' '

    print(phrase.strip())

smash(['    hello', 'world', 'this', 'is', 'great  '])
smash(['Olá', 'tudo em?'])
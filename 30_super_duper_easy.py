# Crie uma função que retorne o valor multiplicado por 50 e acrescido de 6. 
# Se o valor inserido for uma string, a função deve retornar "Erro".

def problem(value):
    return 'Error' if isinstance(value, str) else value * 50 + 6

print(problem(50))
print(problem('testando'))
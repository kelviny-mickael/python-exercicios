# Escreva a função bmi que calcula o índice de massa corporal (imc = peso / altura 2 ).
# se IMC <= 18,5 retornar "Abaixo do peso".
# se IMC <= 25,0 retornar "Normal".
# se IMC <= 30,0 retornar "Sobrepeso".
# se IMC > 30 retorne "Obeso"

def imc(weight, height):
    result_imc = (weight / height ** 2)

    if result_imc <= 18.5:
        return 'Underweight'
    elif result_imc <= 25.0:
        return 'Normal'
    elif result_imc <= 30.0:
        return 'Overweight'
    elif result_imc > 30:
        return 'Obese'
    else:
        return 'Procure um médico imediatamente!!!'

weight = int(input('Enter your wwight: '))
height = float(input('Enter your height: '))

imc(weight, height)
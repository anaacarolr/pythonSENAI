# Calculadora IMC: Crie uma função que receba dois parâmetros que serão o peso(kg) e a altura(m) de uma pessoa e retorne seu IMC.



#  IMC = peso / (altura x altura)



# Depois crie outra função que receba um numero como parâmetro que será o IMC e retorne a classificação de acordo com a figura a seguir.

def conta_imc (peso, altura) : 
    imc_conta = peso / (altura * altura)
    return imc_conta

def classificacao (imc) :
    if imc <= 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 <= 24.9:
        print("Peso normal")
    elif imc >= 25:
        print("Sobrepeso")
    elif imc >= 30:
        print("Obesidade")
    
peso = float(input("DIGITE SEU PESO: "))
altura = float(input("DIGITE SUA ALTURA: "))
imc = conta_imc(peso, altura)
print("seu imc é", imc)
classificacao(imc)


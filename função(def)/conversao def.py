# 2 - Conversor de Temperatura: Crie uma função que receba uma temperatura em graus Celsius como parâmetro e retorne o valor convertido para Fahrenheit e outra para Kelvin.
    
def celsius_para_fahrenheit(graus):
    conversao_fahrenheit = graus * 1.8 + 32
    return conversao_fahrenheit

def celsius_parakelvin(kelvin) :
    conversao_kelvin = graus + 273
    return conversao_kelvin

def mostrar_conversao(graus) :
    print("O resultado é", celsius_para_fahrenheit(graus), "em fahrenheit")
    print("O resultado é", celsius_parakelvin((graus), "em kelvin"))
    
    
graus = float(input("QUANTOS GRAUS ESTÁ? "))

mostrar_conversao(graus)
    

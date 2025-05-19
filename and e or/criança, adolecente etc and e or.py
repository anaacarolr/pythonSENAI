a = int(input( " Digite o ano de seu nascimento: "))

idade = 2025 - a

print( "sua idade é: ", idade)

if idade <= 10 : 
    verifica = "CRIANÇA"
    
elif idade <= 17 :
    verifica = "ADOLESCENTE"
    
elif idade <= 59 :
    verifica = "ADULTO"
    
elif idade >= 60 and idade <= 116:
    verifica = "IDOSO"
else :
    verifica= "INVALIDO"
    
print(verifica)
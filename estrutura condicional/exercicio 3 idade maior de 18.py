#- Solicite o ano de nascimento de uma pessoa, calcule a idade e verifica se a pessoa é maior ou menor de idade e exiba uma mensagem correspondente.
# atividade 3

a = int(input( " Digite o ano de seu nascimento: "))

idade = 2025 - a

print( "sua idade é: ", idade)

if idade > 18 : 
    verifica = "MAIOR DE IDADE"
    
elif idade < 18 :
    verifica = "MENOR DE IDADE"
    
print("Vc está: " , verifica)
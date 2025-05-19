#atividade 2

n = int(input( " Digite sua primeira nota: "))
n2 = int(input(" Digite sua segunda nota: "))
soma = n + n2
media = soma / 2
print( "resultado da média: ", media)

if media > 70 : 
    verifica = "APROVADO"
    
elif media < 70 :
    verifica = "REPROVADO"
    
print("Vc está: " , verifica)
n = int(input( " Digite sua primeira nota: "))
n2 = int(input(" Digite sua segunda nota: "))

if n and n2 <= 100 :
    print("VAlIDO")
    
    soma = n + n2
    media = soma / 2
    print( "resultado da média: ", media)

    if media >= 70 : 
        verifica = "APROVADO"
        
    elif media < 50 :
        verifica = "REPROVADO"
        
    elif  media >= 50 :
        verifica = "RECUPERAÇÃO"
        
    print("Vc está: " , verifica)

else :
    print("INVALIDO")

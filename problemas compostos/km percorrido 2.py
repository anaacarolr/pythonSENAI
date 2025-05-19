# Construa um programa que calcule : Quantos litros de combustível e quantos reais é preciso para fazer uma viagem de 800 quilômetros sendo que o carro tem uma autonomia de 7 km por litro? O carro ainda tem 10  litros no tanque e já percorreu 90  quilômetros da viagem e o preço do combustivel custa R$6,90

print("viagem de carro ")
km = 800 - 90
divisao = km / 7
subtracao = divisao - 10
multiplicacao = divisao * 6.90
print(" quantos litros de combustivel é necessario ", divisao)
print("quantos reais é necessario ", multiplicacao)
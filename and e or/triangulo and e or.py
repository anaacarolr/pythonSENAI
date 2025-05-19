#  Desenvolva um programa que leia os três lados de um triângulo e determine seele é equilátero, isósceles ou escaleno.

#desenvolva um programa que leia os três lados de um triângulo e determine se ele é equilátero, isósceles ou escaleno

#triangulo_equilatero = tres lados iguais, com amesma medida
#triangulo_isosceles = dois lados iguais e um diferente
#triangulo_escaleno = todos os lados diferentes

lado1 = int(input("digite um lado do triângulo: "))
lado2 = int(input("digite um segundo lado do triângulo: "))
lado3 = int(input("digite um terceiro lado do triângulo: "))

if lado1 == lado2 and lado2 == lado3:
    print("o triângulo é equilátero")
elif lado1 == lado2 and lado2 != lado3:
    print("o triângulo é isóceles")
elif lado1 != lado2 and lado2 != lado3:
    print("O triângulo é escaleno")
elif lado1 != lado2 and lado2 == lado3:
    print("o triângulo é isóceles")

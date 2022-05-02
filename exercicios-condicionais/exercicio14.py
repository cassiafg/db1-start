#Faça um Programa que peça os três lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
lado1 = float(input("Primeiro lado: "))
lado2 = float(input("Segundo lado: "))
lado3 = float(input("Terceiro lado: "))
if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1:
    print("Não é um triângulo")
elif lado1 == lado2 == lado3:
    print("Triângulo equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")

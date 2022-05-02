# Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
print("maior: ", maior)
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
print("menor: ", menor)
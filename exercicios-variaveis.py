#1.Faça um Programa que mostre a mensagem "Alo mundo" na tela.
mensagem = 'Alo mundo'
print(mensagem)

#2.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = int(input('Digite um número: '))
print('O número informado foi ', numero)

#3.Faça um Programa que peça dois números e imprima a soma.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('Soma = ',num1 + num2)

#4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
print('Média = ', (nota1 + nota2 + nota3 + nota4)/4)

#5.Faça um Programa que converta metros para centímetros.
metro = float(input('Digite o valor em metros: '))
print(metro, 'm equivale a ', metro * 100, 'cm')

#6.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input('Digite o raio do círculo: '))
area = 3,14 * raio * raio
print('A área do círculo é ', area)

#7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input('Digite o valor do lado: '))
area = lado * lado
print(area * 2)

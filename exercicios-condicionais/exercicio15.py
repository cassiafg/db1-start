#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
print(a,"x2 + ", b, "x + ", c)
delta = (b**2 - 4*a*c)
x1 = ((-b) + (delta**0.5))/(2*a)
x2 = ((-b) - (delta**0.5))/(2*a)
if delta > 0:
    print("x1 = ", x1)
    print("x2 = ", x2)
elif delta == 0:
    print("x1 = x2 = ", x1)
elif delta < 0:
    print("Não possui raízes reais")
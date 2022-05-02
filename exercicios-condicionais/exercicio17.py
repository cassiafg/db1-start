#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
d = int(input("Digite o dia: "))
m = int(input("Digite o mês: "))
a = int(input("Digite o ano: "))
if d>0 and d<=31 and m>0 and m<=12 and a >0:
    if (m == 1 or m== 3 or m==5 or m==7 or m==8 or m==10 or m==12) and (d > 0 and d <= 31):
        print("A data ", d,"/",m,"/",a, "é válida")
    elif (m == 4 or m == 6 or m == 9 or m == 11) and (d> 0 and d <= 30):
        print("A data ", d,"/",m,"/",a, "é válida")
    elif (m == 2):
        if (d > 0 and d <= 29) and (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            print("A data ", d,"/",m,"/",a, "é válida")
        elif (d > 0 and d <= 28) and (a % 4 != 0 and a % 100 == 0) or (a % 400 != 0):
            print("A data ", d,"/",m,"/",a, "é válida")
else:
    print("A data ", d,"/",m,"/",a, "não é válida")
'''2 - Faça um programa que veja se a pessoa tem altura suficiente para andar na montanha russa (120 cm). 
Caso tenha altura, veja se é maior ou menor de idade. 
Caso seja maior de idade (18 anos), o valor do ingresso é x. 
Caso tenha entre 12 e 17, o valor é x/2. 
Caso seja menor de 12 anos o valor é x/3.'''


altura = float(input("digite a sua altura em centimetros:"))
idade = int(input("digite a sua idade:"))
x = 50

if altura >= 120 : 
    if idade >= 18 : 
        ingresso = x
        print(f'o valor do ingresso para a idade de {idade} é R$ {ingresso:,.2f}')
    elif idade >= 12 and idade <= 17 : 
        ingresso = x/2
        print(f'o valor do ingresso para a idade de {idade} é R$ {ingresso:,.2f}')
    elif idade < 12 :
        ingresso = x/3
        print(f'o valor do ingresso para a idade de {idade} é R$ {ingresso:,.2f}')

else: 
    print("vc não tem altura o suficiente D:")





'''4 - Aprimore seu programa de calculo do ingresso da montanha russa e pergunte se o usuario deseja comprar as fotos do passeio.
Estipule um valor x e faca o calculo total do ingresso + fotos.'''

'''altura = float(input("digite a sua altura em centimetros:"))
x = 50
fotos = 20
if altura >= 120 : 
        idade = int(input("digite a sua idade:"))
        resposta = input("deseja comprar as fotos junto com o ingresso? S/N").upper()
        if resposta == 'S'  :
            if idade >= 18 :
                ingresso = x+fotos
                print(f'o valor do ingresso com as fotos para a idade de {idade} é R$ {ingresso:,.2f}')
            elif idade >= 12 and idade <= 17 : 
                ingresso = (x/2)+fotos
                print(f'o valor do ingresso com as fotos para a idade de {idade} é R$ {ingresso:,.2f}')
            elif idade < 12 :
                ingresso = (x/3) + fotos
                print(f'o valor do ingresso com as fotos para a idade de {idade} é R$ {ingresso:,.2f}')
        else : 
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
    print("vc não tem altura o suficiente D:")'''


x = 50 
fotos = 20 

while True: 
    altura = int(input("digite a sua altura:"))
    if altura >= 120 :
        idade = int(input("digite a sua idade"))
        if idade >= 18 : 
            resposta = input("você deseja comprar as fotos? S/N ").upper()
            if resposta == 'S':
                ingresso = x + fotos
                print(f' o valor do ingresso com as fotos é de R${ingresso:,.2f}')
            
            else: 
                ingresso = x 
                print(f'o valor do ingresso para a idade de {idade} é R$ {ingresso:,.2f}')
                break
        
        elif idade >= 12 and idade <= 17 :
            resposta = input("você deseja comprar as fotos? S/N ").upper()
            if resposta == 'S':
                ingresso = (x/2) + fotos
                print(f' o valor do ingresso com as fotos é de R${ingresso:,.2f}')
            else: 
                ingresso = x/2
                print(f'o valor do ingresso para a idade de {idade} é R$ {ingresso:,.2f}')
                break
                    
        elif idade < 12 :            
            resposta = input("você deseja comprar as fotos? S/N ").upper()
            if resposta == 'S':              
                ingresso = (x/3) + fotos
                print(f' o valor do ingresso com as fotos é de R${ingresso:,.2f}')
            else:
                ingresso = x/3
                print(f'o valor do ingresso para a idade de {idade} é R$ {ingresso:,.2f}')
                break
              
    else: 
        print("você não tem a altura permitida! D: \t digite a altura correta só pode acima de 120cm ")
        
    
    
    




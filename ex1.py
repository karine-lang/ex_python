'''
1 - Faça um programa que retorne se o número digitado pelo usuário seja PAR ou IMPAR. Trate e previna possíveis erros de digitação
	Ex : Digitar uma letra, um símbolo, etc. '''


# fiz primeiro dessa forma e não achei muito eficiente
'''while True:
    try:
        numero = int(input("digite um numero: "))
        if numero == ';.,][~´abcdefghijklmnopqrstuvxzwy!@#$%¨&*()-+=':
            raise ValueError(
                "vc digitou um simbolo ou letra pode voltar novamente:")
        if numero % 2 == 0:
            print(f'seu numero é {numero} e ele par')
        else:
            print(f'seu numero é {numero} e ele é impar')
    except ValueError as e:
        print("valor invalido:", e)
    else:
        break'''


while True:


        numero = input("digite um numero:")
        if numero.isdecimal(): 
            if int(numero) % 2 == 0:
                print(f'o {numero} é par')
                break
            else:
                print(f'o {numero} é impar')
                break

        else:
            print("digite um numero inteiro valido")
 
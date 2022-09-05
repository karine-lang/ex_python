'''5 - Faça um jogo de pedra papel e tesoura, com contagem de placar e opção de jogar novamente.
'''
from random import randint
itens = ('PEDRA','PAPEL', 'TESOURA')
computador = randint(0,2) 
placar_jogador = 0
placar_computador = 0 

while True:
    try:
        print('=='*30)
        print(f"( 1 ) = PEDRA\n( 2 ) = PAPEL\n( 3 ) = TESOURA")
        print('=='*30)
        jogador = int(input("DIGITE A JOGADA: \t"))
        print('=='*30)
        print(f'O COMPUTADOR JOGOU {itens[computador-1]}\nO JOGADOR JOGOU {itens[jogador-1]}')
       
    
        if computador == 0 :
            if jogador == 0:
                print("EMPATE, NINGUEM PONTUOU")
            elif jogador == 1:
                placar_jogador+= 1
                print(f"JOGADOR FEZ {placar_jogador} PONTO(S)")
            elif jogador == 2:
                placar_computador+= 1 
                print(f"COMPUTADOR FEZ {placar_computador} PONTO(S) ")
        elif computador == 1:
            if jogador == 0:
                placar_computador+= 1
                print(f"computador fez {placar_computador}")
            elif jogador == 1:
                print("EMPATE, NINGUEM PONTUOU")
            
            elif jogador == 2:
                placar_jogador+= 1
                print(f"JOGADOR FEZ {placar_jogador} PONTO(S)")
        elif computador == 2 :
            if jogador == 0 :
                placar_jogador+= 1  
                print(f"JOGADOR FEZ {placar_jogador} PONTO(S)")
            elif jogador == 1:
                placar_computador+= 1 
                print(f"COMPUTADOR FEZ {placar_computador} PONTO(S)")
            elif jogador == 2:        
                print("EMPATE, NINGUEM PONTUOU")
        if placar_computador >= 5 : 
                print(f"O COMPUTADOR VENCEU COM  {placar_computador} PONTOS")
                break
        elif placar_jogador >= 5 : 
                print(f'O JOGADOR VENCEU COM  {placar_jogador} PONTOS ')
                break
        print('=='*30)
        op = input("DESEJA JOGAR NOVAMENTE: S/N ").upper()
        print('=='*30)
        if op == 'S' :
            continue
        elif op == 'N':
            print(f'O PLACAR FINAL FICOU:\n{placar_computador} PARA O COMPUTADOR\n{placar_jogador} PARA O JOGADOR')
            break
        else:            
            print("VC DIGITOU UMA OPÇÃO INVALIDA, TENTE NOVAMENTE COM S OU N ")
                  
    except IndexError as e : 
        print('=='*30)
        print(f'OPÇÃO INVALIDA TENTE NOVAMENTE: {e}')    
        print('=='*30)

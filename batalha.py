import random




def criar_tabuleiro():
    tabuleiro = []
    linha = ["  1 2 3 4 5"]
    tabuleiro.append(linha)
    for x in range(5):
        linha = [f"{x+1}"] + ["-"] * 5
        tabuleiro.append(linha)
    return tabuleiro




def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))




def posicionar_navios(tabuleiro):
    navios = []
    while len(navios) != 3:
        linha = random.randint(1, 5)
        coluna = random.randint(1, 5)
        if [linha,coluna] not in navios:
            navios.append([linha, coluna])
            tabuleiro[linha][coluna] = "-"
    return navios




def jogar_batalha_naval():
    tabuleiro = criar_tabuleiro()
    navios = posicionar_navios(tabuleiro)
    tentativas = 10




    print("Bem-vindo ao Jogo de Batalha Naval!")
    print("Seu objetivo é afundar os 3 navios inimigos escondidos no tabuleiro!")
    print("Você terá 10 chances de afundar os navios.")
    print("Boa Sorte!")




    while tentativas > 0:
        print(f"Tentativas restantes: {tentativas}")
        exibir_tabuleiro(tabuleiro)




        linha = int(input("Escolha a linha (1 a 5): "))
        coluna = int(input("Escolha a coluna (1 a 5): "))




        if linha < 1 or linha > 5 or coluna < 1 or coluna > 5:
            print("Jogada inválida! Tente novamente.")
            continue




        if tabuleiro[linha][coluna] == "X" or tabuleiro[linha][coluna] == "X":
            print("Você já jogou nessa posição! Tente novamente.")
            continue




        if [linha, coluna] in navios:
            print("Parabéns! Você acertou um navio!")
            tabuleiro[linha][coluna] = "X"
            navios.remove([linha, coluna])
            if len(navios) == 0:
                print("Parabéns! Você destruiu todos os navios!")
                break
        else:
            print("Você errou!")




        tabuleiro[linha][coluna] = "X"
        tentativas -= 1




    if tentativas == 0:
        print("Suas tentativas acabaram. Fim de jogo!")  
           


while True:
    pergunta = input("Pronto para jogar BATALHA DO NAVAL DO MAU? [S/N] \n")
    if pergunta == "S":
        jogar_batalha_naval()
        pergunta = input("Jogar Novamente, [S/N]\n")
        if pergunta == "S":
            continue
        else:
            break
    elif pergunta == "N":
        break
    else:
        print("Pergunta invalida, tente novamente")

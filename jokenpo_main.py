import random
from jokenpo_modulo_comparacao import modulo_comparacao
from jokenpo_modulo_calcula_resultado import calcula_resultado


guarda_resultado = []
apresentacao = """\n\t\tVamos jogar Jokenpô?
\t\tSerão 5 rodadas no total, então o sistema apresentará o vencedor.
\t\tVamos lá!
"""
separador = "\t\t-----------------------------------------------------------------"
print(apresentacao)


rodadas = 0
while rodadas < 5:


    simbolos = ("Pedra", "Tesoura", "Papel")
    computador = random.choice(simbolos)
    print(separador)
    print(f"\t\tRodada: {rodadas+1}")
    menu = """\t\tEscolha entre: 
\t\t[1] Pedra;
\t\t[2] Tesoura;
\t\t[3] Papel"""
    print(menu)
    opcao = int(input("\t\tInforme agora a opção escolhida: "))
    if opcao == 1:
        jogador = "Pedra"
        modulo_comparacao(jogador=jogador, computador=computador, guarda_resultado=guarda_resultado)  ### argumentos nomeados
    elif opcao == 2:
        jogador = "Tesoura"
        modulo_comparacao(jogador=jogador, computador=computador, guarda_resultado=guarda_resultado)  ### argumentos nomeados
    elif opcao == 3:
        jogador = "Papel"
        modulo_comparacao(jogador=jogador, computador=computador, guarda_resultado=guarda_resultado)  ### argumentos nomeados
    else:
        pass


    rodadas += 1


calcula_resultado(guarda_resultado)


print("\t\tFim do programa.")




def calcula_resultado(guarda_resultado):


    resultado_empate = guarda_resultado.count(0)
    empate = resultado_empate
    resultado_jogador_vence = guarda_resultado.count(1)
    jogador_vence = resultado_jogador_vence
    resultado_computador_vence = guarda_resultado.count(2)
    computador_vence = resultado_computador_vence


    if jogador_vence == 2 and computador_vence == 2:
        print("\t\t-----------------------------------------------------------------")
        print(f"\t\tA PARTIDA EMPATOU.\n")
        print(f"\t\tESTATÍSTICAS")
        print(f"\t\tSeu número de vitórias: {jogador_vence}")
        print(f"\t\tNúmero de vitórias do computador: {computador_vence}")
        print(f"\t\tNúmero de empates: {empate}    *obs: valor descartado!")
    elif jogador_vence == 1 and computador_vence >= 2:
        print("\t\t-----------------------------------------------------------------")
        print(f"\t\tO COMPUTADOR VENCEU.\n")
        print(f"\t\tESTATÍSTICAS")
        print(f"\t\tSeu número de vitórias: {jogador_vence}")
        print(f"\t\tNúmero de vitórias do computador: {computador_vence}")
        print(f"\t\tNúmero de empates: {empate}")
    elif jogador_vence >= 2 and computador_vence == 1:
        print("\t\t-----------------------------------------------------------------")
        print(f"\t\tVOCÊ VENCEU.\n")
        print(f"\t\tESTATÍSTICAS")
        print(f"\t\tSeu número de vitórias: {jogador_vence}")
        print(f"\t\tNúmero de vitórias do computador: {computador_vence}")
        print(f"\t\tNúmero de empates: {empate}")
    elif empate >= 3:
        print("\t\t-----------------------------------------------------------------")
        print(f"\t\tA PARTIDA EMPATOU.\n")
        print(f"\t\tESTATÍSTICAS")
        print(f"\t\tSeu número de vitórias: {jogador_vence}")
        print(f"\t\tNúmero de vitórias do computador: {computador_vence}")
        print(f"\t\tNúmero de empates: {empate}")
    elif jogador_vence >= 3 and computador_vence <= 2:
        print("\t\t-----------------------------------------------------------------")
        print(f"\t\tVOCÊ VENCEU.\n")
        print(f"\t\tESTATÍSTICAS")
        print(f"\t\tSeu número de vitórias: {jogador_vence}")
        print(f"\t\tNúmero de vitórias do computador: {computador_vence}")
        print(f"\t\tNúmero de empates: {empate}")
    elif jogador_vence <= 2 and computador_vence >= 3:
        print("\t\t-----------------------------------------------------------------")
        print(f"\t\tO COMPUTADOR VENCEU.\n")
        print(f"\t\tESTATÍSTICAS")
        print(f"\t\tSeu número de vitórias: {jogador_vence}")
        print(f"\t\tNúmero de vitórias do computador: {computador_vence}")
        print(f"\t\tNúmero de empates: {empate}")
    else:
        pass

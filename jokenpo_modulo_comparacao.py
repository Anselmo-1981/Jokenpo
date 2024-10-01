def modulo_comparacao(computador, jogador, guarda_resultado):


    print()


    if computador == "Pedra" and jogador == "Pedra":
        print(f"\t\tJokenpô...")
        print(f"\t\tVOCÊ: {jogador}    vs    Computador: {computador}")
        tipo_resultado = 0
        guarda_resultado.append(tipo_resultado)
        resultado = "\t\tO jogo empatou."
        print(resultado.upper())
        return tipo_resultado

    elif computador == "Pedra" and jogador == "Tesoura":
        print(f"\t\tJokenpô...")
        print(f"\t\tVOCÊ: {jogador}    vs    Computador: {computador}")
        tipo_resultado = 2
        guarda_resultado.append(tipo_resultado)
        resultado = f"\t\tO computador ganhou."
        print(resultado.upper())
        return tipo_resultado

    elif computador == "Pedra" and jogador == "Papel":
        print(f"\t\tJokenpô...")
        print(f"\t\tVOCÊ: {jogador}    vs    Computador: {computador}")
        tipo_resultado = 1
        guarda_resultado.append(tipo_resultado)
        resultado = f"\t\tVocê ganhou!"
        print(resultado.upper())
        return tipo_resultado

    elif computador == "Tesoura" and jogador == 2:
        print(f"\t\tJokenpô...")
        print(f"\t\tVOCÊ: {jogador}    vs    Computador: {computador}")
        tipo_resultado = 0
        guarda_resultado.append(tipo_resultado)
        resultado = "\t\tO jogo empatou."
        print(resultado.upper())
        return tipo_resultado

    elif computador == "Tesoura" and jogador == "Pedra":
        print(f"\t\tJokenpô...")
        print(f"\t\tVOCÊ: {jogador}    vs    Computador: {computador}")
        tipo_resultado = 1
        guarda_resultado.append(tipo_resultado)
        resultado = f"\t\tVocê ganhou!"
        print(resultado.upper())
        return tipo_resultado

    elif computador == "Tesoura" and jogador == "Papel":
        print(f"\t\tJokenpô...")
        print(f"\t\tVOCÊ: {jogador}    vs    Computador: {computador}")
        tipo_resultado = 2
        guarda_resultado.append(tipo_resultado)
        resultado = f"\t\tO computador ganhou."
        print(resultado.upper())
        return tipo_resultado

    elif computador == "Papel" and jogador == "Papel":
        print(f"\t\tJokenpô...")
        print(f"\t\tVOCÊ: {jogador}    vs    Computador: {computador}")
        tipo_resultado = 0
        guarda_resultado.append(tipo_resultado)
        resultado = f"\t\tO jogo empatou."
        print(resultado.upper())
        return tipo_resultado

    elif computador == "Papel" and jogador == "Tesoura":
        print(f"\t\tJokenpô...")
        print(f"\t\tVOCÊ: {jogador}    vs    Computador: {computador}")
        tipo_resultado = 1
        guarda_resultado.append(tipo_resultado)
        resultado = f"\t\tVocê ganhou!"
        print(resultado.upper())
        return tipo_resultado

    elif computador == "Papel" and jogador == "Pedra":
        print(f"\t\tJokenpô...")
        print(f"\t\tVOCÊ: {jogador}    vs    Computador: {computador}")
        tipo_resultado = 2
        guarda_resultado.append(tipo_resultado)
        resultado = f"\t\tO computador ganhou."
        print(resultado.upper())
        return tipo_resultado

    else:
        pass







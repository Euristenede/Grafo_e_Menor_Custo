def duplica_pesos(peso_total_grafo):
    lista_de_chave = []
    lista_de_valor = []
    lista_de_chave_duplicada = []
    lista_de_valor_duplicado = []

    # Captuta os dados do dicionário e separa em duas lista
    # Uma lista contém as chaves e outra tem os valores
    for key, value in peso_total_grafo.items():
        chave = [key]
        valor = value
        lista_de_chave.append(chave)
        lista_de_valor.append(valor)

    # Adiciona uma lista de chaves com valoers duplicados, bidirecional
    for a in range(0, len(lista_de_chave)):
        for w, e in lista_de_chave[a]:
            lista_de_chave_duplicada.append((w, e))
            lista_de_chave_duplicada.append((e, w))

    # Duplica os valores da lista de valores do dicionário
    for b in range(0, len(lista_de_valor)):
        lista_de_valor_duplicado.append(lista_de_valor[b])
        lista_de_valor_duplicado.append(lista_de_valor[b])

    # Gera um novo dicionário com os valores duplicados
    dicionario = zip(lista_de_chave_duplicada, lista_de_valor_duplicado)
    peso_geral = dict(dicionario)

    return peso_geral
import networkx as nx

def cria_grafo():
    G = nx.Graph()

    # adicionando vertices
    for i in range(1,78):
        G.add_node(i)

    #primeira linha
    G.add_edge(1, 2, weight=100); G.add_edge(2, 3, weight=100); G.add_edge(3, 4, weight=100); G.add_edge(4, 5, weight=100);
    G.add_edge(5, 6, weight=100); G.add_edge(6, 7, weight=100); G.add_edge(7, 8, weight=110); G.add_edge(8, 9, weight=190);
    #primeira linha para segunda linha
    G.add_edge(1, 10, weight=170); G.add_edge(2, 11, weight=170); G.add_edge(3, 12, weight=170); G.add_edge(4, 13, weight=170);
    G.add_edge(5, 14, weight=170); G.add_edge(6, 15, weight=170); G.add_edge(7, 16, weight=170); G.add_edge(8, 17, weight=170);
    G.add_edge(9, 19, weight=170);
    #segunda linha
    G.add_edge(10, 11, weight=100); G.add_edge(11, 12, weight=100); G.add_edge(12, 13, weight=100); G.add_edge(13, 14, weight=100);
    G.add_edge(14, 15, weight=100); G.add_edge(15, 16, weight=100); G.add_edge(16, 17, weight=100); G.add_edge(17, 18, weight=100);
    G.add_edge(18, 19, weight=100); G.add_edge(19, 20, weight=100);
    #segunda linha para terceira linha
    G.add_edge(10, 21, weight=170); G.add_edge(11, 22, weight=170); G.add_edge(12, 23, weight=170); G.add_edge(13, 24, weight=170);
    G.add_edge(14, 25, weight=170); G.add_edge(15, 26, weight=170); G.add_edge(16, 27, weight=170); G.add_edge(17, 28, weight=170);
    G.add_edge(18, 29, weight=170); G.add_edge(19, 30, weight=170); G.add_edge(20, 31, weight=170);
    #terceira linha
    G.add_edge(21, 22, weight=90); G.add_edge(22, 23, weight=100); G.add_edge(23, 24, weight=100); G.add_edge(24, 25, weight=100);
    G.add_edge(25, 26, weight=100); G.add_edge(26, 27, weight=100); G.add_edge(27, 28, weight=100); G.add_edge(28, 29, weight=100);
    G.add_edge(29, 30, weight=100); G.add_edge(30, 31, weight=100);
    #terceira linha para quarta linha
    G.add_edge(26, 32, weight=100);
    #terceira e quarta linha para quinta linha
    G.add_edge(21, 33, weight=170); G.add_edge(22, 34, weight=170); G.add_edge(23, 35, weight=170); G.add_edge(24, 36, weight=170);
    G.add_edge(25, 37, weight=170); G.add_edge(32, 38, weight=100); G.add_edge(32, 39, weight=100); G.add_edge(27, 40, weight=170);
    G.add_edge(28, 41, weight=170); G.add_edge(29, 42, weight=170); G.add_edge(30, 43, weight=170); G.add_edge(31, 44, weight=170);
    #quinta linha
    G.add_edge(33, 34, weight=90); G.add_edge(34, 35, weight=100); G.add_edge(35, 36, weight=100); G.add_edge(36, 37, weight=100);
    G.add_edge(37, 38, weight=48); G.add_edge(38, 45, weight=100); G.add_edge(45, 39, weight=100); G.add_edge(39, 40, weight=48);
    G.add_edge(40, 41, weight=100); G.add_edge(41, 42, weight=100); G.add_edge(42, 43, weight=100); G.add_edge(43, 44, weight=100);
    #sexta linha para sétima linha
    G.add_edge(45, 51, weight=110);
    #quinta linha para sétima linha
    G.add_edge(33, 46, weight=170); G.add_edge(34, 47, weight=170); G.add_edge(35, 48, weight=170); G.add_edge(36, 49, weight=170);
    G.add_edge(37, 50, weight=170); G.add_edge(40, 52, weight=170); G.add_edge(41, 53, weight=170); G.add_edge(42, 54, weight=170);
    G.add_edge(43, 55, weight=170); G.add_edge(44, 56, weight=170);
    #sétima linha
    G.add_edge(46, 47, weight=90); G.add_edge(47, 48, weight=100); G.add_edge(48, 49, weight=100); G.add_edge(49, 50, weight=100);
    G.add_edge(50, 51, weight=100); G.add_edge(51, 52, weight=100); G.add_edge(52, 53, weight=100); G.add_edge(53, 54, weight=100);
    G.add_edge(54, 55, weight=100); G.add_edge(55, 56, weight=100);
    #sétima linha para oitava linha
    G.add_edge(46, 57, weight=170); G.add_edge(47, 58, weight=170); G.add_edge(48, 59, weight=170); G.add_edge(49, 60, weight=170);
    G.add_edge(50, 61, weight=170); G.add_edge(51, 62, weight=170); G.add_edge(52, 63, weight=170); G.add_edge(53, 64, weight=170);
    G.add_edge(54, 65, weight=170); G.add_edge(55, 66, weight=170); G.add_edge(56, 67, weight=170);
    #oitava linha
    G.add_edge(57, 58, weight=100); G.add_edge(58, 59, weight=100); G.add_edge(59, 60, weight=100); G.add_edge(60, 61, weight=100);
    G.add_edge(61, 62, weight=100); G.add_edge(62, 63, weight=100); G.add_edge(63, 64, weight=100); G.add_edge(64, 65, weight=100);
    G.add_edge(65, 66, weight=100); G.add_edge(66, 67, weight=100);
    #oitava linha para nona linha
    G.add_edge(57, 68, weight=170); G.add_edge(58, 69, weight=170); G.add_edge(59, 70, weight=170); G.add_edge(60, 71, weight=170);
    G.add_edge(61, 72, weight=170); G.add_edge(62, 73, weight=170); G.add_edge(63, 74, weight=170); G.add_edge(64, 75, weight=170);
    G.add_edge(65, 76, weight=170); G.add_edge(66, 77, weight=170); G.add_edge(67, 78, weight=170);
    #nona linha
    G.add_edge(68, 69, weight=110); G.add_edge(69, 70, weight=90); G.add_edge(70, 71, weight=90); G.add_edge(71, 72, weight=90);
    G.add_edge(72, 73, weight=90); G.add_edge(73, 74, weight=90); G.add_edge(74, 75, weight=90); G.add_edge(75, 76, weight=90);
    G.add_edge(76, 77, weight=90); G.add_edge(77, 78, weight=90);

    return G

#Retorna o menor caminho entre dois pontos
def menor_caminho(G ,ponto_inicial, ponto_final):
    caminho = nx.dijkstra_path(G, ponto_inicial, ponto_final)
    return caminho

#Retorna o peso de um caminho
def peso_do_caminho(caminho, peso_geral):
    x = 0
    for j in range(0, len(caminho) - 1):
        x += peso_geral[(caminho[j], caminho[j + 1])]
    return x
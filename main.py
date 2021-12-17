
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:57:14 2021

@author: euris
"""
import matplotlib.pyplot as plt
import networkx as nx
import grafo
import pesos

#Recebe o grafo
G = grafo.cria_grafo()

#Recebe o peso de cada aresta
peso_total_grafo = nx.get_edge_attributes(G,'weight')

#Duplica os pesos do grafo, Bidirecional
peso_geral = pesos.duplica_pesos(peso_total_grafo)


ponto_inicial = 9
pontos_a_percorrer = [23, 45, 65, 12, 17]

pontos = []
pontos.append(ponto_inicial)
pontos.extend(pontos_a_percorrer)

G1 = nx.Graph()
# adicionando vertices
for i in pontos:
    G1.add_node(i)

lista_de_nos = []
lista_de_pesos = []

for j in range(0, len(pontos)):
    for k in range(0, len(pontos)):
        a = grafo.menor_caminho(G, pontos[j], pontos[k])
        b = grafo.peso_do_caminho(a, peso_geral)
        G1.add_edge(pontos[j], pontos[k], weight=b);
        lista_de_nos.append((pontos[j], pontos[k]))
        lista_de_pesos.append(b)

dicionario = zip(lista_de_nos, lista_de_pesos)
peso_total = dict(dicionario)
menor_peso = 9999
a = 0
b = 0
lista_menor_peso = []
lista_caminho = []
for i in range(0, len(pontos)):
    i = 0
    if len(pontos) == 1:
        break
    for j in range(0, len(pontos)-1):
        m = grafo.menor_caminho(G1, pontos[i], pontos[j+1])
        n = grafo.peso_do_caminho(m, peso_total)
        if n < menor_peso:
            menor_peso = n
            a = pontos[i]
            b = pontos[j+1]
    lista_menor_peso.append(menor_peso)
    lista_caminho.append([(a,b)])
    pontos.remove(a)
    pontos.remove(b)
    pontos.insert(0, b)
    menor_peso = 9999
    if len(pontos) == 1:
        lista_caminho.append([(b, ponto_inicial)])
#Mostra a melhor rota, Objetivo do trabalho
print(lista_caminho)

lista_completa = []
for a in range(0, len(lista_caminho)):
    for w, e in lista_caminho[a]:
        d = grafo.menor_caminho(G, w, e)
        lista_completa.append(d)
print(lista_completa)

#G1._node[4]['pos'] = (0,0)
#G1._node[53]['pos'] = (2,2)
#G1._node[31]['pos'] = (2,-2)
#G1._node[77]['pos'] = (4,2)
#G1._node[38]['pos'] = (5,-2)
#G1._node[6]['pos'] = (7,-1)

# plota o grafo
nx.draw(G, with_labels=True,  node_size = 500)
#nx.draw_networkx(G1, nx.get_node_attributes(G1,'pos'),node_color=['red'], node_size=450)
#nx.draw_networkx_edges(G1, nx.get_node_attributes(G1,'pos'),edge_color= ['red'])
#nx.draw_networkx_edge_labels(G1, nx.get_node_attributes(G1,'pos') ,edge_labels=nx.get_edge_attributes(G1,'weight'))
#plt.axis('off')
plt.show()
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia


from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *


g_eu2 = MeuGrafo(['1', '2', '3', '4', '5', '6', '7'])
g_eu2.adicionaAresta('a1', '1', '2')
g_eu2.adicionaAresta('a2', '2', '3')
g_eu2.adicionaAresta('a4', '3', '4')
g_eu2.adicionaAresta('a5', '4', '5')
g_eu2.adicionaAresta('a8', '5', '6')
g_eu2.adicionaAresta('a9', '6', '7')
print(g_eu2.euler())

g_eu3 = MeuGrafo(['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'])
g_eu3.adicionaAresta('a1', 'A', 'B')
g_eu3.adicionaAresta('a2', 'B', 'C')
g_eu3.adicionaAresta('a3', 'C', 'D')
g_eu3.adicionaAresta('a4', 'F', 'D')
g_eu3.adicionaAresta('a5', 'A', 'D')
g_eu3.adicionaAresta('a6', 'F', 'G')
g_eu3.adicionaAresta('a7', 'G', 'H')
g_eu3.adicionaAresta('a8', 'H', 'I')
g_eu3.adicionaAresta('a9', 'I', 'F')
print(g_eu3.euler())

g_eu4 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
g_eu4.adicionaAresta('a1', 'A', 'B')
g_eu4.adicionaAresta('a2', 'A', 'C')
g_eu4.adicionaAresta('a3', 'B', 'F')
g_eu4.adicionaAresta('a4', 'A', 'D')
g_eu4.adicionaAresta('a5', 'C', 'E')
g_eu4.adicionaAresta('a6', 'E', 'B')
g_eu4.adicionaAresta('a7', 'B', 'G')
g_eu4.adicionaAresta('a8', 'G', 'D')
g_eu4.adicionaAresta('a9', 'A', 'A')
print(g_eu4.euler())

g_eu5 = MeuGrafo(['1', '2', '3', '4'])
g_eu5.adicionaAresta('a1', '1', '2')
g_eu5.adicionaAresta('a2', '2', '3')
g_eu5.adicionaAresta('a3', '3', '1')
g_eu5.adicionaAresta('a4', '1', '4')
print(g_eu5.euler())
import unittest
from meu_grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *


class TestGrafo(unittest.TestCase):

    def setUp(self):

        # Grafos desconexos

        self.dex1 = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.dex1.adicionaAresta('a1', 'A', 'B')
        self.dex1.adicionaAresta('a3', 'A', 'D')
        self.dex1.adicionaAresta('a4', 'B', 'E')
        self.dex1.adicionaAresta('a5', 'B', 'F')
        self.dex1.adicionaAresta('a6', 'B', 'G')
        self.dex1.adicionaAresta('a7', 'C', 'H')
        self.dex1.adicionaAresta('a8', 'C', 'I')
        self.dex1.adicionaAresta('a9', 'C', 'J')

        self.dex2 = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.dex2.adicionaAresta('a4', 'B', 'E')
        self.dex2.adicionaAresta('a5', 'B', 'F')
        self.dex2.adicionaAresta('a6', 'B', 'G')
        self.dex2.adicionaAresta('a7', 'C', 'H')
        self.dex2.adicionaAresta('a8', 'C', 'I')
        self.dex2.adicionaAresta('a9', 'C', 'J')

        self.dex3 = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.dex3.adicionaAresta('a1', 'A', 'B')
        self.dex3.adicionaAresta('a3', 'B', 'D')
        self.dex3.adicionaAresta('a4', 'B', 'E')
        self.dex3.adicionaAresta('a5', 'B', 'F')
        self.dex3.adicionaAresta('a6', 'B', 'C')
        self.dex3.adicionaAresta('a7', 'C', 'H')
        self.dex3.adicionaAresta('a8', 'C', 'I')
        self.dex3.adicionaAresta('a9', 'C', 'J')

        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')



        # Grafos Vazios
        self.g_v = MeuGrafo()

        # Grafos Um nó
        self.g_n = MeuGrafo(['A'])

        # Grafo Arvore Médio
        self.g_d1_J = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_d1_J.adicionaAresta('a1', 'A', 'B')
        self.g_d1_J.adicionaAresta('a2', 'A', 'C')
        self.g_d1_J.adicionaAresta('a3', 'A', 'D')
        self.g_d1_J.adicionaAresta('a4', 'B', 'E')
        self.g_d1_J.adicionaAresta('a5', 'B', 'F')
        self.g_d1_J.adicionaAresta('a6', 'B', 'G')
        self.g_d1_J.adicionaAresta('a7', 'C', 'H')
        self.g_d1_J.adicionaAresta('a8', 'C', 'I')
        self.g_d1_J.adicionaAresta('a9', 'C', 'J')
        self.g_d1_J.adicionaAresta('a10', 'E', 'K')
        self.g_d1_J.adicionaAresta('a11', 'E', 'L')
        self.g_d1_J.adicionaAresta('a12', 'E', 'M')
        self.g_d1_J.adicionaAresta('a13', 'F', 'N')
        self.g_d1_J.adicionaAresta('a14', 'F', 'O')
        self.g_d1_J.adicionaAresta('a15', 'F', 'P')
        self.g_d1_J.adicionaAresta('a16', 'G', 'Q')
        self.g_d1_J.adicionaAresta('a17', 'G', 'R')
        self.g_d1_J.adicionaAresta('a18', 'G', 'S')
        self.g_d1_J.adicionaAresta('a19', 'H', 'T')
        self.g_d1_J.adicionaAresta('a20', 'H', 'U')
        self.g_d1_J.adicionaAresta('a21', 'H', 'V')
        self.g_d1_J.adicionaAresta('a22', 'I', 'W')
        self.g_d1_J.adicionaAresta('a23', 'I', 'X')
        self.g_d1_J.adicionaAresta('a24', 'I', 'Y')
        self.g_d1_J.adicionaAresta('a25', 'W', 'Z')

        # Grafo arvore grande

        self.g_d2_J = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
             '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
             '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50'])
        self.g_d2_J.adicionaAresta('a1', '1', '2')
        self.g_d2_J.adicionaAresta('a2', '2', '3')
        self.g_d2_J.adicionaAresta('a3', '3', '4')
        self.g_d2_J.adicionaAresta('a4', '4', '5')
        self.g_d2_J.adicionaAresta('a5', '5', '6')
        self.g_d2_J.adicionaAresta('a6', '5', '7')
        self.g_d2_J.adicionaAresta('a7', '5', '8')
        self.g_d2_J.adicionaAresta('a8', '5', '9')
        self.g_d2_J.adicionaAresta('a9', '5', '10')
        self.g_d2_J.adicionaAresta('a10', '6', '11')
        self.g_d2_J.adicionaAresta('a11', '6', '12')
        self.g_d2_J.adicionaAresta('a12', '6', '13')
        self.g_d2_J.adicionaAresta('a13', '6', '14')
        self.g_d2_J.adicionaAresta('a14', '6', '15')
        self.g_d2_J.adicionaAresta('a15', '6', '16')
        self.g_d2_J.adicionaAresta('a16', '6', '17')
        self.g_d2_J.adicionaAresta('a17', '6', '18')
        self.g_d2_J.adicionaAresta('a18', '6', '19')
        self.g_d2_J.adicionaAresta('a19', '7', '20')
        self.g_d2_J.adicionaAresta('a20', '7', '21')
        self.g_d2_J.adicionaAresta('a21', '7', '22')
        self.g_d2_J.adicionaAresta('a22', '7', '23')
        self.g_d2_J.adicionaAresta('a23', '7', '24')
        self.g_d2_J.adicionaAresta('a24', '7', '25')
        self.g_d2_J.adicionaAresta('a25', '7', '26')
        self.g_d2_J.adicionaAresta('a26', '7', '27')
        self.g_d2_J.adicionaAresta('a27', '7', '28')
        self.g_d2_J.adicionaAresta('a28', '7', '29')
        self.g_d2_J.adicionaAresta('a29', '11', '30')
        self.g_d2_J.adicionaAresta('a30', '30', '31')
        self.g_d2_J.adicionaAresta('a31', '30', '32')
        self.g_d2_J.adicionaAresta('a32', '30', '33')
        self.g_d2_J.adicionaAresta('a33', '30', '34')
        self.g_d2_J.adicionaAresta('a34', '30', '35')
        self.g_d2_J.adicionaAresta('a35', '30', '36')
        self.g_d2_J.adicionaAresta('a36', '30', '37')
        self.g_d2_J.adicionaAresta('a37', '30', '38')
        self.g_d2_J.adicionaAresta('a38', '30', '39')
        self.g_d2_J.adicionaAresta('a39', '20', '40')
        self.g_d2_J.adicionaAresta('a40', '40', '41')
        self.g_d2_J.adicionaAresta('a41', '40', '42')
        self.g_d2_J.adicionaAresta('a42', '40', '43')
        self.g_d2_J.adicionaAresta('a43', '40', '44')
        self.g_d2_J.adicionaAresta('a44', '40', '45')
        self.g_d2_J.adicionaAresta('a45', '40', '46')
        self.g_d2_J.adicionaAresta('a46', '40', '47')
        self.g_d2_J.adicionaAresta('a47', '40', '48')
        self.g_d2_J.adicionaAresta('a48', '40', '49')
        self.g_d2_J.adicionaAresta('a49', '49', '50')
        self.g_d2_J.adicionaAresta('a50', '50', '50')
        # Grafos teste dfs e bfs
        self.g_pdfs = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_pdfs.adicionaAresta('a1', 'J', 'C')
        self.g_pdfs.adicionaAresta('a2', 'C', 'E')
        self.g_pdfs.adicionaAresta('a4', 'P', 'C')
        self.g_pdfs.adicionaAresta('a6', 'T', 'C')
        self.g_pdfs.adicionaAresta('a8', 'M', 'T')
        self.g_pdfs.adicionaAresta('a9', 'T', 'Z')

        self.g_pbfs = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_pbfs.adicionaAresta('a1', 'J', 'C')
        self.g_pbfs.adicionaAresta('a2', 'C', 'E')
        self.g_pbfs.adicionaAresta('a4', 'P', 'C')
        self.g_pbfs.adicionaAresta('a6', 'T', 'C')
        self.g_pbfs.adicionaAresta('a7', 'M', 'C')
        self.g_pbfs.adicionaAresta('a9', 'T', 'Z')

        self.g_cd = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_cd.adicionaAresta('a1', 'J', 'C')
        self.g_cd.adicionaAresta('a4', 'E', 'C')
        self.g_cd.adicionaAresta('a6', 'P', 'E')

        self.g_cb = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_cb.adicionaAresta('a1', 'J', 'C')
        self.g_cb.adicionaAresta('a2', 'J', 'E')
        self.g_cb.adicionaAresta('a3', 'J', 'P')

        self.g_l5d = MeuGrafo(['C', 'D'])
        self.g_l5d.adicionaAresta('a1', 'D', 'C')

        self.g_d1_Jd = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_d1_Jd.adicionaAresta('a1', 'A', 'B')
        self.g_d1_Jd.adicionaAresta('a2', 'A', 'C')
        self.g_d1_Jd.adicionaAresta('a3', 'A', 'D')
        self.g_d1_Jd.adicionaAresta('a4', 'B', 'E')
        self.g_d1_Jd.adicionaAresta('a5', 'B', 'F')
        self.g_d1_Jd.adicionaAresta('a6', 'B', 'G')
        self.g_d1_Jd.adicionaAresta('a7', 'C', 'H')
        self.g_d1_Jd.adicionaAresta('a8', 'C', 'I')
        self.g_d1_Jd.adicionaAresta('a9', 'C', 'J')
        self.g_d1_Jd.adicionaAresta('a10', 'E', 'K')
        self.g_d1_Jd.adicionaAresta('a11', 'E', 'L')
        self.g_d1_Jd.adicionaAresta('a12', 'E', 'M')
        self.g_d1_Jd.adicionaAresta('a13', 'F', 'N')
        self.g_d1_Jd.adicionaAresta('a14', 'F', 'O')
        self.g_d1_Jd.adicionaAresta('a15', 'F', 'P')
        self.g_d1_Jd.adicionaAresta('a16', 'G', 'Q')
        self.g_d1_Jd.adicionaAresta('a17', 'G', 'R')
        self.g_d1_Jd.adicionaAresta('a18', 'G', 'S')
        self.g_d1_Jd.adicionaAresta('a19', 'H', 'T')
        self.g_d1_Jd.adicionaAresta('a20', 'H', 'U')
        self.g_d1_Jd.adicionaAresta('a21', 'H', 'V')
        self.g_d1_Jd.adicionaAresta('a22', 'I', 'W')
        self.g_d1_Jd.adicionaAresta('a23', 'I', 'X')
        self.g_d1_Jd.adicionaAresta('a24', 'I', 'Y')
        self.g_d1_Jd.adicionaAresta('a25', 'W', 'Z')

        self.g_d2_Jd = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
             '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
             '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50'])
        self.g_d2_Jd.adicionaAresta('a1', '1', '2')
        self.g_d2_Jd.adicionaAresta('a2', '2', '3')
        self.g_d2_Jd.adicionaAresta('a3', '3', '4')
        self.g_d2_Jd.adicionaAresta('a4', '4', '5')
        self.g_d2_Jd.adicionaAresta('a5', '5', '6')
        self.g_d2_Jd.adicionaAresta('a6', '5', '7')
        self.g_d2_Jd.adicionaAresta('a7', '5', '8')
        self.g_d2_Jd.adicionaAresta('a8', '5', '9')
        self.g_d2_Jd.adicionaAresta('a9', '5', '10')
        self.g_d2_Jd.adicionaAresta('a10', '6', '11')
        self.g_d2_Jd.adicionaAresta('a11', '6', '12')
        self.g_d2_Jd.adicionaAresta('a12', '6', '13')
        self.g_d2_Jd.adicionaAresta('a13', '6', '14')
        self.g_d2_Jd.adicionaAresta('a14', '6', '15')
        self.g_d2_Jd.adicionaAresta('a15', '6', '16')
        self.g_d2_Jd.adicionaAresta('a16', '6', '17')
        self.g_d2_Jd.adicionaAresta('a17', '6', '18')
        self.g_d2_Jd.adicionaAresta('a18', '6', '19')
        self.g_d2_Jd.adicionaAresta('a19', '7', '20')
        self.g_d2_Jd.adicionaAresta('a20', '7', '21')
        self.g_d2_Jd.adicionaAresta('a21', '7', '22')
        self.g_d2_Jd.adicionaAresta('a22', '7', '23')
        self.g_d2_Jd.adicionaAresta('a23', '7', '24')
        self.g_d2_Jd.adicionaAresta('a24', '7', '25')
        self.g_d2_Jd.adicionaAresta('a25', '7', '26')
        self.g_d2_Jd.adicionaAresta('a26', '7', '27')
        self.g_d2_Jd.adicionaAresta('a27', '7', '28')
        self.g_d2_Jd.adicionaAresta('a28', '7', '29')
        self.g_d2_Jd.adicionaAresta('a29', '11', '30')
        self.g_d2_Jd.adicionaAresta('a30', '30', '31')
        self.g_d2_Jd.adicionaAresta('a31', '30', '32')
        self.g_d2_Jd.adicionaAresta('a32', '30', '33')
        self.g_d2_Jd.adicionaAresta('a33', '30', '34')
        self.g_d2_Jd.adicionaAresta('a34', '30', '35')
        self.g_d2_Jd.adicionaAresta('a35', '30', '36')
        self.g_d2_Jd.adicionaAresta('a36', '30', '37')
        self.g_d2_Jd.adicionaAresta('a37', '30', '38')
        self.g_d2_Jd.adicionaAresta('a38', '30', '39')
        self.g_d2_Jd.adicionaAresta('a39', '20', '40')
        self.g_d2_Jd.adicionaAresta('a40', '40', '41')
        self.g_d2_Jd.adicionaAresta('a41', '40', '42')
        self.g_d2_Jd.adicionaAresta('a42', '40', '43')
        self.g_d2_Jd.adicionaAresta('a43', '40', '44')
        self.g_d2_Jd.adicionaAresta('a44', '40', '45')
        self.g_d2_Jd.adicionaAresta('a45', '40', '46')
        self.g_d2_Jd.adicionaAresta('a46', '40', '47')
        self.g_d2_Jd.adicionaAresta('a47', '40', '48')
        self.g_d2_Jd.adicionaAresta('a48', '40', '49')
        self.g_d2_Jd.adicionaAresta('a49', '49', '50')

        # Matrizes para teste do algoritmo de Warshall

        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1', 'J', 'C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        # Grafo com ciclos e laços
        self.g_e = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.g_e.adicionaAresta('1', 'A', 'B')
        self.g_e.adicionaAresta('2', 'A', 'C')
        self.g_e.adicionaAresta('3', 'C', 'A')
        self.g_e.adicionaAresta('4', 'C', 'B')
        self.g_e.adicionaAresta('10', 'C', 'B')
        self.g_e.adicionaAresta('5', 'C', 'D')
        self.g_e.adicionaAresta('6', 'D', 'D')
        self.g_e.adicionaAresta('7', 'D', 'B')
        self.g_e.adicionaAresta('8', 'D', 'E')
        self.g_e.adicionaAresta('9', 'E', 'A')
        self.g_e.adicionaAresta('11', 'E', 'B')

        #Grafo Dj
        self.g_d2_Jk = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
             '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33'])
        self.g_d2_Jk.adicionaAresta('a0', '1', '2')
        self.g_d2_Jk.adicionaAresta('a1', '1', '3')
        self.g_d2_Jk.adicionaAresta('a2', '1', '4')
        self.g_d2_Jk.adicionaAresta('a3', '2', '5')
        self.g_d2_Jk.adicionaAresta('a4', '5', '6')
        self.g_d2_Jk.adicionaAresta('a5', '6', '2')
        self.g_d2_Jk.adicionaAresta('a6', '3', '7')
        self.g_d2_Jk.adicionaAresta('a7', '7', '6')
        self.g_d2_Jk.adicionaAresta('a8', '4', '8')
        self.g_d2_Jk.adicionaAresta('a9', '8', '7')
        self.g_d2_Jk.adicionaAresta('a10', '2', '9')
        self.g_d2_Jk.adicionaAresta('a11', '6', '10')
        self.g_d2_Jk.adicionaAresta('a12', '7', '10')
        self.g_d2_Jk.adicionaAresta('a13', '10', '9')
        self.g_d2_Jk.adicionaAresta('a14', '7', '11')
        self.g_d2_Jk.adicionaAresta('a15', '8', '12')
        self.g_d2_Jk.adicionaAresta('a16', '9', '13')
        self.g_d2_Jk.adicionaAresta('a17', '10', '14')
        self.g_d2_Jk.adicionaAresta('a18', '11', '15')
        self.g_d2_Jk.adicionaAresta('a19', '12', '16')
        self.g_d2_Jk.adicionaAresta('a20', '13', '17')
        self.g_d2_Jk.adicionaAresta('a21', '13', '19')
        self.g_d2_Jk.adicionaAresta('a22', '14', '18')
        self.g_d2_Jk.adicionaAresta('a23', '14', '19')
        self.g_d2_Jk.adicionaAresta('a24', '14', '20')
        self.g_d2_Jk.adicionaAresta('a25', '15', '19')
        self.g_d2_Jk.adicionaAresta('a26', '16', '20')
        self.g_d2_Jk.adicionaAresta('a27', '16', '21')
        self.g_d2_Jk.adicionaAresta('a28', '17', '22')
        self.g_d2_Jk.adicionaAresta('a29', '17', '21')
        self.g_d2_Jk.adicionaAresta('a30', '18', '17')
        self.g_d2_Jk.adicionaAresta('a31', '18', '22')
        self.g_d2_Jk.adicionaAresta('a32', '19', '18')
        self.g_d2_Jk.adicionaAresta('a33', '19', '24')
        self.g_d2_Jk.adicionaAresta('a34', '21', '25')
        self.g_d2_Jk.adicionaAresta('a35', '21', '26')
        self.g_d2_Jk.adicionaAresta('a36', '22', '26')
        self.g_d2_Jk.adicionaAresta('a37', '22', '27')
        self.g_d2_Jk.adicionaAresta('a38', '22', '23')
        self.g_d2_Jk.adicionaAresta('a39', '23', '19')
        self.g_d2_Jk.adicionaAresta('a40', '24', '28')
        self.g_d2_Jk.adicionaAresta('a41', '24', '29')
        self.g_d2_Jk.adicionaAresta('a42', '25', '30')
        self.g_d2_Jk.adicionaAresta('a43', '28', '31')
        self.g_d2_Jk.adicionaAresta('a44', '30', '31')
        self.g_d2_Jk.adicionaAresta('a45', '31', '32')
        self.g_d2_Jk.adicionaAresta('a46', '31', '33')


        # Matrizes para teste do algoritmo de Warshall

        self.g_p_m = self.constroi_matriz(self.g_p)
        self.g_p_m[0][1] = 1
        self.g_p_m[0][2] = 1
        self.g_p_m[1][2] = 1
        self.g_p_m[3][1] = 1
        self.g_p_m[3][2] = 1
        self.g_p_m[4][1] = 1
        self.g_p_m[4][2] = 1
        self.g_p_m[4][5] = 1
        self.g_p_m[4][6] = 1
        self.g_p_m[5][1] = 1
        self.g_p_m[5][2] = 1
        self.g_p_m[5][6] = 1

        self.g_e_m = self.constroi_matriz(self.g_e)
        for i in range(0, len(self.g_e_m)):
            self.g_e_m[0][i] = 1
            self.g_e_m[2][i] = 1
            self.g_e_m[3][i] = 1
            self.g_e_m[4][i] = 1
        self.g_c_m = self.constroi_matriz(self.g_c)
        self.g_c_m[0][1] = 1
        self.g_c_m[0][2] = 1
        self.g_c_m[0][3] = 1
        self.g_c_m[2][1] = 1
        self.g_c_m[3][1] = 1
        self.g_c_m[3][2] = 1

        # Matrizes para teste do algoritmo de Khan

        self.EngC = MeuGrafo(
            ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '31', '32', '33', '34',
             '35', '36', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62', '63', '64', '65', '71',
             '72',
             '72', '73', '74', '75', '81', '82', '83', '84', '85', '91', '92', '93', '94', 'Op1', '101', '102', '103',
             'Op2',
             'Op3'])
        self.EngC.adicionaAresta('a0', '11', '21')
        self.EngC.adicionaAresta('a1', '21', '31')
        self.EngC.adicionaAresta('a2', '21', '41')
        self.EngC.adicionaAresta('a3', '31', '51')
        self.EngC.adicionaAresta('a4', '51', '61')
        self.EngC.adicionaAresta('a5', '34', '81')
        self.EngC.adicionaAresta('a6', '35', '81')
        self.EngC.adicionaAresta('a7', '54', '81')
        self.EngC.adicionaAresta('a8', '31', '52')
        self.EngC.adicionaAresta('a9', '43', '62')
        self.EngC.adicionaAresta('a10', '24', '72')
        self.EngC.adicionaAresta('a11', '73', '82')
        self.EngC.adicionaAresta('a12', '83', '92')
        self.EngC.adicionaAresta('a13', '24', '33')
        self.EngC.adicionaAresta('a14', '24', '43')
        self.EngC.adicionaAresta('a15', '24', '53')
        self.EngC.adicionaAresta('a16', '34', '63')
        self.EngC.adicionaAresta('a17', '35', '63')
        self.EngC.adicionaAresta('a18', '63', '73')
        self.EngC.adicionaAresta('a19', '74', '83')
        self.EngC.adicionaAresta('a20', '44', '93')
        self.EngC.adicionaAresta('a21', '45', '93')
        self.EngC.adicionaAresta('a22', '92', '103')
        self.EngC.adicionaAresta('a23', '14', '24')
        self.EngC.adicionaAresta('a24', '15', '24')
        self.EngC.adicionaAresta('a25', '14', '34')
        self.EngC.adicionaAresta('a26', '15', '34')
        self.EngC.adicionaAresta('a27', '24', '44')
        self.EngC.adicionaAresta('a28', '36', '44')
        self.EngC.adicionaAresta('a29', '24', '54')
        self.EngC.adicionaAresta('a30', '31', '64')
        self.EngC.adicionaAresta('a31', '61', '84')
        self.EngC.adicionaAresta('a32', '64', '84')
        self.EngC.adicionaAresta('a33', '61', '94')
        self.EngC.adicionaAresta('a34', '75', '94')
        self.EngC.adicionaAresta('a35', '14', '25')
        self.EngC.adicionaAresta('a36', '15', '25')
        self.EngC.adicionaAresta('a37', '14', '35')
        self.EngC.adicionaAresta('a38', '15', '35')
        self.EngC.adicionaAresta('a39', '36', '45')
        self.EngC.adicionaAresta('a40', '36', '55')
        self.EngC.adicionaAresta('a41', '44', '55')
        self.EngC.adicionaAresta('a42', '55', '65')
        self.EngC.adicionaAresta('a43', '52', '75')
        self.EngC.adicionaAresta('a44', '64', '75')
        self.EngC.adicionaAresta('a45', '75', '85')
        self.EngC.adicionaAresta('a46', '16', '26')
        self.EngC.adicionaAresta('a47', '26', '36')

        self.Telematica = MeuGrafo(
            ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '31', '32', '33', '34',
             '35', '36', '37', '41', '42', '43', '44', '45', '46', '47', '51', '52', '53', '54', '55', '56', '57', '61',
             '62', '63', '64', '65', '66', 'TCC', 'Estagio',
             ])
        self.Telematica.adicionaAresta('a0', '11', '21')
        self.Telematica.adicionaAresta('a1', '12', '22')
        self.Telematica.adicionaAresta('a2', '16', '22')
        self.Telematica.adicionaAresta('a3', '12', '23')
        self.Telematica.adicionaAresta('a4', '16', '23')
        self.Telematica.adicionaAresta('a5', '13', '24')
        self.Telematica.adicionaAresta('a6', '16', '26')
        self.Telematica.adicionaAresta('a7', '21', '31')
        self.Telematica.adicionaAresta('a8', '26', '32')
        self.Telematica.adicionaAresta('a9', '22', '33')
        self.Telematica.adicionaAresta('a10', '23', '33')
        self.Telematica.adicionaAresta('a11', '26', '33')
        self.Telematica.adicionaAresta('a12', '14', '34')
        self.Telematica.adicionaAresta('a13', '25', '35')
        self.Telematica.adicionaAresta('a14', '21', '36')
        self.Telematica.adicionaAresta('a15', '24', '36')
        self.Telematica.adicionaAresta('a16', '31', '41')
        self.Telematica.adicionaAresta('a17', '31', '42')
        self.Telematica.adicionaAresta('a18', '32', '43')
        self.Telematica.adicionaAresta('a19', '32', '44')
        self.Telematica.adicionaAresta('a20', '33', '44')
        self.Telematica.adicionaAresta('a21', '33', '45')
        self.Telematica.adicionaAresta('a22', '21', '46')
        self.Telematica.adicionaAresta('a23', '34', '46')
        self.Telematica.adicionaAresta('a24', '41', '51')
        self.Telematica.adicionaAresta('a25', '41', '52')
        self.Telematica.adicionaAresta('a26', '44', '53')
        self.Telematica.adicionaAresta('a27', '44', '54')
        self.Telematica.adicionaAresta('a28', '37', '55')
        self.Telematica.adicionaAresta('a29', '41', '55')
        self.Telematica.adicionaAresta('a30', '44', '55')
        self.Telematica.adicionaAresta('a31', '42', '61')
        self.Telematica.adicionaAresta('a32', '51', '61')
        self.Telematica.adicionaAresta('a33', '53', '62')
        self.Telematica.adicionaAresta('a34', '55', 'TCC')
        self.Telematica.adicionaAresta('a35', '37', 'Estagio')
        self.Telematica.adicionaAresta('a36', '41', 'Estagio')
        self.Telematica.adicionaAresta('a37', '44', 'Estagio')

        self.Fisica = MeuGrafo(
            ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '31', '32', '33', '34',
             '35', '36', '37', '41', '42', '43', '44', '45', '46', '51', '52', '53', '54', '55', '56', '57', '61', '62',
             '63', '64', '65', '66', '68', '71', '72',
             '72', '73', '74', '75', '76', '81', '82', '83', '84', '85', '86'])
        self.Fisica.adicionaAresta('a0', '11', '21')
        self.Fisica.adicionaAresta('a1', '12', '21')
        self.Fisica.adicionaAresta('a2', '11', '22')
        self.Fisica.adicionaAresta('a3', '12', '22')
        self.Fisica.adicionaAresta('a4', '12', '23')
        self.Fisica.adicionaAresta('a5', '12', '24')
        self.Fisica.adicionaAresta('a6', '14', '24')
        self.Fisica.adicionaAresta('a7', '15', '25')
        self.Fisica.adicionaAresta('a8', '21', '31')
        self.Fisica.adicionaAresta('a9', '23', '31')
        self.Fisica.adicionaAresta('a10', '21', '32')
        self.Fisica.adicionaAresta('a11', '22', '32')
        self.Fisica.adicionaAresta('a12', '23', '33')
        self.Fisica.adicionaAresta('a13', '31', '41')
        self.Fisica.adicionaAresta('a14', '31', '42')
        self.Fisica.adicionaAresta('a15', '32', '42')
        self.Fisica.adicionaAresta('a16', '33', '45')
        self.Fisica.adicionaAresta('a17', '31', '46')
        self.Fisica.adicionaAresta('a18', '41', '51')
        self.Fisica.adicionaAresta('a19', '45', '51')
        self.Fisica.adicionaAresta('a20', '41', '52')
        self.Fisica.adicionaAresta('a21', '42', '52')
        self.Fisica.adicionaAresta('a22', '45', '53')
        self.Fisica.adicionaAresta('a23', '31', '54')
        self.Fisica.adicionaAresta('a24', '43', '55')
        self.Fisica.adicionaAresta('a25', '21', '57')
        self.Fisica.adicionaAresta('a26', '43', '57')
        self.Fisica.adicionaAresta('a27', '51', '61')
        self.Fisica.adicionaAresta('a28', '51', '62')
        self.Fisica.adicionaAresta('a29', '52', '62')
        self.Fisica.adicionaAresta('a30', '21', '63')
        self.Fisica.adicionaAresta('a31', '53', '63')
        self.Fisica.adicionaAresta('a32', '51', '64')
        self.Fisica.adicionaAresta('a33', '56', '66')
        self.Fisica.adicionaAresta('a34', '31', '68')
        self.Fisica.adicionaAresta('a35', '57', '68')
        self.Fisica.adicionaAresta('a36', '61', '71')
        self.Fisica.adicionaAresta('a37', '41', '72')
        self.Fisica.adicionaAresta('a38', '45', '72')
        self.Fisica.adicionaAresta('a39', '66', '73')
        self.Fisica.adicionaAresta('a40', '31', '74')
        self.Fisica.adicionaAresta('a41', '43', '74')
        self.Fisica.adicionaAresta('a42', '41', '76')
        self.Fisica.adicionaAresta('a43', '68', '76')
        self.Fisica.adicionaAresta('a44', '65', '81')
        self.Fisica.adicionaAresta('a45', '74', '82')
        self.Fisica.adicionaAresta('a46', '73', '83')
        self.Fisica.adicionaAresta('a47', '54', '84')
        self.Fisica.adicionaAresta('a48', '71', '84')
        self.Fisica.adicionaAresta('a49', '16', '85')
        self.Fisica.adicionaAresta('a50', '25', '85')
        self.Fisica.adicionaAresta('a51', '51', '86')
        self.Fisica.adicionaAresta('a52', '76', '86')

        self.Const_ed = MeuGrafo(
            ['11', '12', '13', '14', '15', '16', '17', '18', '21', '22', '23', '24', '25', '26', '27', '31', '32', '33',
             '34', '35', '36', '37', '38', '41', '42', '43', '44', '45', '46', '47', '51', '52', '53', '54', '55', '56',
             '57', '58', '61', '62', '63', '64', '65', '66', '67', '68', '71', '72',
             '72', '73'])
        self.Const_ed.adicionaAresta('a0', '15', '21')
        self.Const_ed.adicionaAresta('a1', '14', '23')
        self.Const_ed.adicionaAresta('a2', '11', '24')
        self.Const_ed.adicionaAresta('a3', '17', '24')
        self.Const_ed.adicionaAresta('a4', '15', '25')
        self.Const_ed.adicionaAresta('a5', '17', '26')
        self.Const_ed.adicionaAresta('a6', '17', '27')
        self.Const_ed.adicionaAresta('a7', '15', '32')
        self.Const_ed.adicionaAresta('a8', '21', '32')
        self.Const_ed.adicionaAresta('a9', '21', '33')
        self.Const_ed.adicionaAresta('a10', '25', '33')
        self.Const_ed.adicionaAresta('a11', '15', '34')
        self.Const_ed.adicionaAresta('a12', '11', '35')
        self.Const_ed.adicionaAresta('a13', '27', '35')
        self.Const_ed.adicionaAresta('a14', '26', '36')
        self.Const_ed.adicionaAresta('a15', '23', '37')
        self.Const_ed.adicionaAresta('a16', '24', '38')
        self.Const_ed.adicionaAresta('a17', '17', '41')
        self.Const_ed.adicionaAresta('a18', '21', '41')
        self.Const_ed.adicionaAresta('a19', '17', '42')
        self.Const_ed.adicionaAresta('a20', '21', '42')
        self.Const_ed.adicionaAresta('a21', '23', '43')
        self.Const_ed.adicionaAresta('a22', '24', '44')
        self.Const_ed.adicionaAresta('a23', '36', '54')
        self.Const_ed.adicionaAresta('a24', '37', '45')
        self.Const_ed.adicionaAresta('a25', '21', '45')
        self.Const_ed.adicionaAresta('a26', '17', '46')
        self.Const_ed.adicionaAresta('a27', '32', '46')
        self.Const_ed.adicionaAresta('a28', '11', '47')
        self.Const_ed.adicionaAresta('a29', '37', '47')
        self.Const_ed.adicionaAresta('a30', '37', '51')
        self.Const_ed.adicionaAresta('a31', '43', '51')
        self.Const_ed.adicionaAresta('a32', '45', '51')
        self.Const_ed.adicionaAresta('a33', '46', '51')
        self.Const_ed.adicionaAresta('a34', '41', '52')
        self.Const_ed.adicionaAresta('a35', '42', '52')
        self.Const_ed.adicionaAresta('a36', '45', '52')
        self.Const_ed.adicionaAresta('a37', '46', '52')
        self.Const_ed.adicionaAresta('a38', '17', '53')
        self.Const_ed.adicionaAresta('a39', '32', '53')
        self.Const_ed.adicionaAresta('a40', '47', '54')
        self.Const_ed.adicionaAresta('a41', '17', '55')
        self.Const_ed.adicionaAresta('a42', '32', '55')
        self.Const_ed.adicionaAresta('a43', '46', '56')
        self.Const_ed.adicionaAresta('a44', '43', '57')
        self.Const_ed.adicionaAresta('a45', '31', '62')
        self.Const_ed.adicionaAresta('a46', '44', '62')
        self.Const_ed.adicionaAresta('a47', '22', '64')
        self.Const_ed.adicionaAresta('a48', '27', '64')
        self.Const_ed.adicionaAresta('a49', '33', '64')
        self.Const_ed.adicionaAresta('a50', '36', '64')
        self.Const_ed.adicionaAresta('a51', '47', '65')
        self.Const_ed.adicionaAresta('a52', '22', '66')
        self.Const_ed.adicionaAresta('a52', '31', '67')

        self.Matematica = MeuGrafo(
            ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '31', '32', '33', '34',
             '35', '36', '41', '42', '43', '44', '45', '46', '51', '52', '53', '54', '55', '56', '57', '61', '62', '63',
             '64', '65', '66', '67', '71', '72',
             '72', '73', '74', '75', '76', '77', '81', '82', '83', '84', '85', '86', '87'])
        self.Matematica.adicionaAresta('a0', '11', '21')
        self.Matematica.adicionaAresta('a1', '11', '22')
        self.Matematica.adicionaAresta('a2', '13', '22')
        self.Matematica.adicionaAresta('a3', '16', '26')
        self.Matematica.adicionaAresta('a4', '21', '31')
        self.Matematica.adicionaAresta('a5', '22', '32')
        self.Matematica.adicionaAresta('a6', '12', '33')
        self.Matematica.adicionaAresta('a7', '12', '34')
        self.Matematica.adicionaAresta('a8', '21', '41')
        self.Matematica.adicionaAresta('a9', '23', '41')
        self.Matematica.adicionaAresta('a10', '23', '42')
        self.Matematica.adicionaAresta('a11', '32', '42')
        self.Matematica.adicionaAresta('a12', '36', '43')
        self.Matematica.adicionaAresta('a13', '34', '44')
        self.Matematica.adicionaAresta('a14', '27', '45')
        self.Matematica.adicionaAresta('a15', '33', '51')
        self.Matematica.adicionaAresta('a16', '12', '52')
        self.Matematica.adicionaAresta('a17', '32', '53')
        self.Matematica.adicionaAresta('a18', '44', '54')
        self.Matematica.adicionaAresta('a19', '44', '55')
        self.Matematica.adicionaAresta('a20', '44', '57')
        self.Matematica.adicionaAresta('a21', '51', '61')
        self.Matematica.adicionaAresta('a22', '52', '62')
        self.Matematica.adicionaAresta('a23', '32', '63')
        self.Matematica.adicionaAresta('a24', '54', '64')
        self.Matematica.adicionaAresta('a25', '46', '65')
        self.Matematica.adicionaAresta('a26', '57', '67')
        self.Matematica.adicionaAresta('a27', '42', '71')
        self.Matematica.adicionaAresta('a28', '22', '72')
        self.Matematica.adicionaAresta('a29', '41', '73')
        self.Matematica.adicionaAresta('a30', '42', '73')
        self.Matematica.adicionaAresta('a31', '64', '74')
        self.Matematica.adicionaAresta('a32', '65', '75')
        self.Matematica.adicionaAresta('a33', '67', '77')
        self.Matematica.adicionaAresta('a34', '62', '81')
        self.Matematica.adicionaAresta('a35', '75', '82')
        self.Matematica.adicionaAresta('a36', '32', '83')
        self.Matematica.adicionaAresta('a37', '74', '84')
        self.Matematica.adicionaAresta('a38', '77', '87')


    def constroi_matriz(self, g: MeuGrafo):
        ordem = len(g.N)
        m = list()
        for i in range(ordem):
            m.append(list())
            for j in range(ordem):
                m[i].append(0)
        return m

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_eq(self):
        g_p_eq = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        g_p_eq.adicionaAresta('a1', 'J', 'C')
        g_p_eq.adicionaAresta('a2', 'C', 'E')
        g_p_eq.adicionaAresta('a3', 'C', 'E')
        g_p_eq.adicionaAresta('a4', 'P', 'C')
        g_p_eq.adicionaAresta('a5', 'P', 'C')
        g_p_eq.adicionaAresta('a6', 'T', 'C')
        g_p_eq.adicionaAresta('a7', 'M', 'C')
        g_p_eq.adicionaAresta('a8', 'M', 'T')
        g_p_eq.adicionaAresta('a9', 'T', 'Z')

        g_p_neq = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        g_p_neq.adicionaAresta('a1', 'C', 'C')
        g_p_neq.adicionaAresta('a2', 'C', 'E')
        g_p_neq.adicionaAresta('a3', 'C', 'E')
        g_p_neq.adicionaAresta('a4', 'P', 'C')
        g_p_neq.adicionaAresta('a5', 'P', 'C')
        g_p_neq.adicionaAresta('a6', 'T', 'C')
        g_p_neq.adicionaAresta('a7', 'M', 'C')
        g_p_neq.adicionaAresta('a8', 'M', 'T')
        g_p_neq.adicionaAresta('a9', 'T', 'Z')

        g_p_neq2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])

        self.assertEqual(self.g_p, g_p_eq)
        self.assertNotEqual(self.g_p, g_p_neq)
        self.assertNotEqual(self.g_p, g_p_neq2)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(set(self.g_p.vertices_nao_adjacentes()),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-J', 'C-T', 'C-Z', 'C-M', 'C-P', 'E-C', 'E-J', 'E-P',
                          'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-Z', 'T-J',
                          'T-M', 'T-E', 'T-P', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-T'})

        self.assertEqual(set(self.g_c.vertices_nao_adjacentes()), {'C-J', 'C-E', 'C-P', 'E-J', 'E-P', 'P-J'})
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])
        self.assertEqual(set(self.g_e.vertices_nao_adjacentes()),
                         {'A-D', 'A-E', 'B-A', 'B-C', 'B-D', 'B-E', 'C-E', 'D-C', 'D-A', 'E-D', 'E-C'})

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())
        self.assertTrue(self.g_e.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)
        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_e.grau('C'), 5)
        self.assertEqual(self.g_e.grau('D'), 5)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())
        self.assertTrue(self.g_e.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), {'a1'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), {'a7', 'a8'})
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), {'a1', 'a2', 'a3'})
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), {'asd'})
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')
        self.assertEqual(set(self.g_e.arestas_sobre_vertice('D')), {'5', '6', '7', '8'})

    def test_warshall(self):
        self.assertEqual((self.g_p.warshall()),self.g_p_m)
        self.assertEqual((self.g_e.warshall()),self.g_e_m)
        self.assertEqual((self.g_c.warshall()), self.g_c_m)

    def test_DiJ(self):
        self.assertEqual(set(self.g_d2_Jk.Dijkstra('1','33',3,3,['12','19','21','30'])), {'1', '4', '8', '12', '16', '21', '25', '30', '31', '33'})

    def test_Khan(self):
        self.assertEqual(set(self.EngC.Khan()),{'11', '12', '13', '14', '15', '16', '17', '22', '23', '27', '32', '42', '71', '74', '91', 'Op1', '101', '102',
         'Op2', 'Op3', '21', '24', '25', '26', '34', '35', '83', '31', '33', '36', '41', '43', '53', '54', '63', '72',
         '92', '44', '45', '51', '52', '62', '64', '73', '81', '103', '55', '61', '75', '82', '93', '65', '84', '85',
         '94'})
        self.assertEqual(set(self.Telematica.Khan()),
                         {'11', '12', '13', '14', '15', '16', '17', '25', '27', '37', '47', '56', '57', '63', '64', '65', '66', '21', '22', '23', '24', '26', '34', '35', '31', '32', '33', '36', '46', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', 'Estagio', '61', '62', 'TCC'
})
        self.assertEqual(set(self.Fisica.Khan()),
                         {'11', '12', '13', '14', '15', '16', '17', '26', '27', '34', '35', '36', '37', '43', '44', '56', '65', '75', '21', '22', '23', '24', '25', '55', '66', '81', '31', '32', '33', '57', '73', '85', '41', '42', '45', '46', '54', '68', '74', '83', '51', '52', '53', '72', '76', '82', '61', '62', '63', '64', '86', '71', '84'
})
        self.assertEqual(set(self.Const_ed.Khan()),
                         {'11', '12', '13', '14', '15', '16', '17', '18', '22', '31', '58', '61', '63', '68', '71', '72', '73', '21', '23', '24', '25', '26', '27', '34', '66', '67', '32', '33', '35', '36', '37', '38', '41', '42', '43', '44', '45', '46', '47', '53', '55', '57', '62', '64', '51', '52', '54', '56', '65'
})
        self.assertEqual(set(self.Matematica.Khan()),
                         {'11', '12', '13', '14', '15', '16', '17', '23', '24', '25', '27', '35', '36', '46', '56', '66', '76', '85', '86', '21', '22', '26', '33', '34', '43', '45', '52', '65', '31', '32', '41', '44', '51', '62', '72', '75', '42', '53', '54', '55', '57', '61', '63', '81', '82', '83', '64', '67', '71', '73', '74', '77', '84', '87'})

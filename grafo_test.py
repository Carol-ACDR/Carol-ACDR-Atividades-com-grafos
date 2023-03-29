
import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
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

        #Eules_testes

        self.g_eu1 = MeuGrafo(['1', '2', '3', '4'])
        self.g_eu1.adicionaAresta('a1', '1', '2')
        self.g_eu1.adicionaAresta('a2', '2', '3')
        self.g_eu1.adicionaAresta('a3', '3', '4')
        self.g_eu1.adicionaAresta('a4', '4', '1')

        self.g_eu2 = MeuGrafo(['1', '2', '3', '4', '5', '6', '7'])
        self.g_eu2.adicionaAresta('a1', '1', '2')
        self.g_eu2.adicionaAresta('a2', '2', '3')
        self.g_eu2.adicionaAresta('a4', '3', '4')
        self.g_eu2.adicionaAresta('a5', '4', '5')
        self.g_eu2.adicionaAresta('a8', '5', '6')
        self.g_eu2.adicionaAresta('a9', '6', '7')

        self.g_eu3 = MeuGrafo(['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'])
        self.g_eu3.adicionaAresta('a1', 'A', 'B')
        self.g_eu3.adicionaAresta('a2', 'B', 'C')
        self.g_eu3.adicionaAresta('a3', 'C', 'D')
        self.g_eu3.adicionaAresta('a4', 'F', 'D')
        self.g_eu3.adicionaAresta('a5', 'A', 'D')
        self.g_eu3.adicionaAresta('a6', 'F', 'G')
        self.g_eu3.adicionaAresta('a7', 'G', 'H')
        self.g_eu3.adicionaAresta('a8', 'H', 'I')
        self.g_eu3.adicionaAresta('a9', 'I', 'F')

        self.g_eu4 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.g_eu4.adicionaAresta('a1', 'A', 'B')
        self.g_eu4.adicionaAresta('a2', 'A', 'C')
        self.g_eu4.adicionaAresta('a3', 'B', 'F')
        self.g_eu4.adicionaAresta('a4', 'A', 'D')
        self.g_eu4.adicionaAresta('a5', 'C', 'E')
        self.g_eu4.adicionaAresta('a6', 'E', 'B')
        self.g_eu4.adicionaAresta('a7', 'B', 'G')
        self.g_eu4.adicionaAresta('a8', 'G', 'D')

        self.g_eu5 = MeuGrafo(['1', '2', '3', '4'])
        self.g_eu5.adicionaAresta('a1', '1', '2')
        self.g_eu5.adicionaAresta('a2', '2', '3')
        self.g_eu5.adicionaAresta('a3', '3', '1')
        self.g_eu5.adicionaAresta('a4', '1', '4')

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
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_v.adicionaAresta('b1', 'A', 'C'))

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_v.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_n.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())
        self.assertFalse(self.g_v.ha_laco())
        self.assertFalse(self.g_n.ha_laco())

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

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

        # Vazio
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_v.grau('G'), 5)

        # Um nó
        self.assertEqual(self.g_n.grau('A'), 0)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())
        self.assertFalse(self.g_v.ha_paralelas())
        self.assertFalse(self.g_n.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')
        with self.assertRaises(VerticeInvalidoException):
            self.g_v.arestas_sobre_vertice('A')
        self.assertEqual(set(self.g_n.arestas_sobre_vertice('A')), set([]))

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertTrue((self.g_v.eh_completo()))
        self.assertTrue((self.g_n.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.g_d1_J.dfs('A'), self.g_d1_Jd)
        self.assertEqual(self.g_d2_J.dfs('1'), self.g_d2_Jd)
        self.assertEqual(self.g_p.dfs('J'), self.g_pdfs)
        self.assertEqual(self.g_c.dfs('J'), self.g_cd)
        self.assertEqual(self.g_l5.dfs('D'), self.g_l5d)

    def test_bfs(self):
        self.assertEqual(self.g_d1_J.bfs('A'), self.g_d1_Jd)
        self.assertEqual(self.g_d2_J.bfs('1'), self.g_d2_Jd)
        self.assertEqual(self.g_pbfs.bfs('J'), self.g_pbfs)
        self.assertEqual(self.g_c.bfs('J'), self.g_cb)
        self.assertEqual(self.g_l5.dfs('D'), self.g_l5d)

    def test_ha_ciclo(self):
        self.assertEqual(set(self.g_p.ha_ciclo()), set(['C', 'a2', 'E', 'a3', 'C']))
        self.assertEqual(set(self.g_p_sem_paralelas.ha_ciclo()), set(['C', 'a4', 'T', 'a6', 'M', 'a5', 'C']))
        self.assertFalse(self.g_c2.ha_ciclo())
        self.assertEqual(set(self.g_c.ha_ciclo()), set(['J', 'a1', 'C', 'a4', 'E', 'a2', 'J']))
        self.assertEqual(set(self.g_l1.ha_ciclo()), set(['A', 'a1', 'A']))
        self.assertFalse(self.g_d1_J.ha_ciclo())
        self.assertEqual(set(self.g_d2_J.ha_ciclo()), set(['50', 'a50', '50']))
    def test_caminho(self):
        self.assertEqual(set(self.g_p.caminho(3)), set(['J', 'a1', 'C', 'a6', 'T','a8','M']))
        self.assertEqual(set(self.g_c2.caminho(1)), set(['Nina', 'amiga', 'Maria']))
        self.assertFalse(self.g_p_sem_paralelas.caminho(5))
        self.assertEqual(set(self.g_d1_J.caminho(5)), set(['B', 'a1', 'A', 'a2', 'C', 'a8', 'I', 'a22', 'W', 'a25', 'Z']))
        self.assertEqual(set(self.g_l1.caminho(1)), set(['A', 'a2', 'B']))
        self.assertFalse(self.g_c.caminho(4))
        self.assertEqual(set(self.g_d2_J.caminho(9)), set(['1', 'a1', '2', 'a2', '3', 'a3', '4', 'a4', '5', 'a6', '7', 'a19', '20', 'a39', '40', 'a48', '49', 'a49', '50']))
    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue((self.g_p_sem_paralelas.conexo()))
        self.assertTrue((self.g_c.conexo()))
        self.assertTrue((self.g_c2.conexo()))
        self.assertTrue((self.g_c3.conexo()))
        self.assertFalse((self.g_l1.conexo()))
        self.assertFalse((self.g_l2.conexo()))
        self.assertFalse((self.g_l3.conexo()))
        self.assertTrue((self.g_l4.conexo()))
        self.assertTrue((self.g_l5.conexo()))
        self.assertTrue((self.g_n.conexo()))
        self.assertTrue((self.g_d1_J.conexo()))
        self.assertTrue((self.g_d2_J.conexo()))
        self.assertFalse((self.g_d.conexo()))
        self.assertFalse((self.dex1.conexo()))
        self.assertFalse((self.dex2.conexo()))
        self.assertFalse((self.dex3.conexo()))
    def test_euler(self):
        self.assertEqual(set(self.g_eu1.euler()), set(['1', 'a1', '2', 'a2', '3', 'a3', '4', 'a4', '1']))
        self.assertEqual(set(self.g_eu2.euler()), set(['1', 'a1', '2', 'a2', '3', 'a4', '4', 'a5', '5', 'a8', '6', 'a9', '7']))
        self.assertFalse(self.dex1.euler())
        self.assertEqual(set(self.g_eu3.euler()), set(['D', 'a3', 'C', 'a2', 'B', 'a1', 'A', 'a5', 'D', 'a4', 'F', 'a6', 'G', 'a7', 'H', 'a8', 'I', 'a9', 'F']))
        self.assertEqual(set(self.g_eu4.euler()), set(['A', 'a1', 'B', 'a6', 'E', 'a5', 'C', 'a2', 'A', 'a4', 'D', 'a8', 'G', 'a7', 'B', 'a3', 'F']))
        self.assertFalse(self.g_p.euler())
        self.assertEqual(set(self.g_eu5.euler()), set(['1', 'a1', '2', 'a2', '3', 'a3', '1', 'a4', '4']))
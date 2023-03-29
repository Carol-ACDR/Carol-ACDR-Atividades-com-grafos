from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        G = []
        H = []

        arestas = self.lista_com_arestas().copy()
        for ar in arestas:
            G.append("{}-{}".format(ar.getV1(), ar.getV2()))
        for v in self.N:
            for v2 in self.N:
                if (("{}-{}".format(v, v2)) in G) or (("{}-{}".format(v2, v)) in G):
                    continue
                else:
                    if (("{}-{}".format(v, v2)) in H) or (("{}-{}".format(v2, v) in H)) or (v == v2):
                        continue
                    else:
                        H.append("{}-{}".format(v, v2))
        return H

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.M)):
            if len(self.M[i][i])>0:
                return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        else:
          Ind = self.N.index(V)
          grau = 0
          for i in range(Ind,len(self.M)):
              if Ind==i:
                  grau += len(self.M[Ind][i])*2
              else:
                  grau+= len(self.M[Ind][i])
          for i2 in range(0,Ind):
              grau+=len(self.M[i2][Ind])
          return grau
    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if (self.M[i][j] != '-'):
                    if len(self.M[i][j])>1:
                        return True
                else:
                    continue
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        else:
            Ind = self.N.index(V)
            arestas = []
            for i in range(Ind, len(self.M)):
                if (self.M[Ind][i] != 'o'):
                  for a in self.M[Ind][i]:
                    arestas.append(a)
            for i2 in range(0, Ind):
                if (self.M[i2][Ind] != 'o'):
                  for a in self.M[i2][Ind]:
                    arestas.append(a)
            return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        arestas = self.lista_com_arestas().copy()
        if (self.ha_laco == True) or (self.ha_paralelas() == True):
            return False
        else:
            s = 0
            k = (len(self.N) - 1)
            for i in range(len(self.N)):
                s += k
                k -= 1
            if len(arestas) != s:
                return False
            else:
                return True
    def lista_com_arestas(self):
        arestas = []
        for V in self.N:
            Ind = self.N.index(V)
            for i in range(Ind, len(self.M)):
                if (self.M[Ind][i] != 'o'):
                    for a in self.M[Ind][i].values():
                        if a not in arestas:
                            arestas.append(a)
            for i2 in range(0, Ind):
                if (self.M[i2][Ind] != 'o'):
                    for a in self.M[i2][Ind].values():
                        if a not in arestas:
                            arestas.append(a)
        return arestas

from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

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
                if ("{}-{}".format(v, v2)) in G:
                    continue
                else:
                    if (("{}-{}".format(v, v2)) in H) or (v == v2):
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
            if len(self.M[i][i]) > 0:
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
            for i in range(len(self.M)):
                if Ind == i:
                    grau += len(self.M[Ind][i]) * 2
                else:
                    grau += len(self.M[Ind][i])
            for i2 in range(len(self.M)):
                if Ind == i2:
                    continue
                else:
                    grau += len(self.M[i2][Ind])
            return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if (self.M[i][j] != '-'):
                    if len(self.M[i][j]) > 1:
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
            for i in range(len(self.M)):
                if (self.M[Ind][i] != 'o'):
                    for a in self.M[Ind][i]:
                        arestas.append(a)
            for i2 in range(len(self.M)):
                if (self.M[i2][Ind] != 'o'):
                    for a in self.M[i2][Ind]:
                        if a not in arestas:
                          arestas.append(a)
                        else:
                            continue
            return arestas
    def arestas_sobre_verticea(self, V):
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
            for i in range(len(self.M)):
                if (self.M[Ind][i] != 'o'):
                    for a in self.M[Ind][i].values():
                        arestas.append(a)
            for i2 in range(len(self.M)):
                if (self.M[i2][Ind] != 'o'):
                    for a in self.M[i2][Ind].values():
                        if a not in arestas:
                          arestas.append(a)
                        else:
                            continue
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
            for i in range(len(self.M)):
                if (self.M[Ind][i] != 'o'):
                    for a in self.M[Ind][i].values():
                        if a not in arestas:
                            arestas.append(a)
            for i2 in range(len(self.M)):
                if (self.M[i2][Ind] != 'o'):
                    for a in self.M[i2][Ind].values():
                        if a not in arestas:
                            arestas.append(a)
        return arestas

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        E = deepcopy(self.M)
        for i in range (0,len(E)):
            for  j in range (0,len(E)):
                if len(E[i][j]) >0:
                    E[i][j] = 1
                else:
                    E[i][j] = 0
        for i in range(0, len(E)):
            for j in range(0, len(E)):
                if E[j][i]== 1:
                    for k in range (0,len(E)):
                        E[j][k] = max(E[j][k],E[i][k])
        return E
    def Dijkstra(self,VP = '',VC = '',CargaInicial = 0,Máxima = 0,Pontos=[]):
        if (VP or VC) not in self.N:
            raise VerticeInvalidoException
        FI1 = [VP]
        pi1 = ['0']
        peso_FI1 = [0]
        FI0 = []
        peso_FI0 = []
        pi0 = []
        W = VP
        Final = []
        CargaP = []
        CargaT = [CargaInicial]
        while W != VC:
            ar = self.arestas_sobre_verticea(W)
            for a in ar:
                indw = FI1.index(W)
                if (a.getV1() == W) and (a.getV1() != a.getV2()) and (a.getV2() not in FI0):
                  FI0.append(a.getV2())
                  peso_FI0.append(a.getPeso()+peso_FI1[indw])
                  pi0.append(W)
                  CargaP.append(CargaT[indw] - a.getPeso())
                elif (a.getV1() == W) and (a.getV1() != a.getV2) and (a.getV2() in FI0):
                    index = FI0.index(a.getV2())
                    if (a.getPeso()+peso_FI1[indw])< peso_FI0[index]:
                        peso_FI0[index] = a.getPeso()+peso_FI1[indw]
                        pi0[index] = W
                        CargaP.append(CargaT[indw] - a.getPeso())
                    else:
                        continue
            if FI0 == []:
                return False
            else:
                indice = peso_FI0.index(min(peso_FI0))
                if (FI0[indice] not in FI1) and (CargaP[indice] >=0):
                  FI1.append(FI0[indice])
                  peso_FI1.append(peso_FI0[indice])
                  pi1.append(pi0[indice])
                  if FI0[indice] in Pontos:
                      CargaT.append(Máxima)
                  else:
                      CargaT.append(CargaP[indice])
                  W = FI0[indice]
                  FI0.pop(indice)
                  peso_FI0.pop(indice)
                  CargaP.pop(indice)
                  pi0.pop(indice)
                elif (FI0[indice] in FI1) and (CargaInicial - peso_FI0[indice] >=0):
                  if (peso_FI0[indice] < peso_FI1[indice]):
                    indF = FI1.index(FI0[indice])
                    FI1[indF] = FI0[indice]
                    peso_FI1[indF] = peso_FI0[indice]
                    pi1[indF] = pi0[indice]
                    W = FI0[indice]
                    if FI0[indice] in Pontos:
                      CargaT[indF] = Máxima
                    else:
                      CargaT[indF] = CargaP[indice]
                    FI0.pop(indice)
                    peso_FI0.pop(indice)
                    pi0.pop(indice)
                    CargaP.pop(indice)
                  else:
                    FI0.pop(indice)
                    peso_FI0.pop(indice)
                    pi0.pop(indice)
                    CargaP.pop(indice)
                else:
                  FI0.pop(indice)
                  peso_FI0.pop(indice)
                  pi0.pop(indice)
                  CargaP.pop(indice)
        while W != '0':
            Final.insert(0,W)
            H = FI1.index(W)
            W = pi1[H]
        return Final

    def Khan(self):
          K = []
          aux = []
          aux2 =[]
          a = self.lista_com_arestas()
          while len(self.N) != 0:
            for b in a:
                if b.getV2() not in aux:
                  aux.append(b.getV2())
            for c in self.N:
                if (c not in aux) and (c not in K):
                    K.append(c)
            for d in a:
                if d.getV1() in K:
                      aux2.append(d)
            for e in aux2:
                if e in a:
                  a.remove(e)
            for f in self.N:
              if f in K:
                self.N.remove(f)
            aux = []
            aux2 = []
          return K


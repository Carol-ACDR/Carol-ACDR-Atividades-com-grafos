from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import deepcopy

class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        G = []
        H = []
        for a in self.A:
          G.append("{}-{}".format(self.A[a].getV1(),self.A[a].getV2()))
        for v in self.N:
          for v2 in self.N:
            if (("{}-{}".format(v,v2)) in G) or (("{}-{}".format(v2,v)) in G):
              continue
            else:
              if (("{}-{}".format(v,v2)) in H) or(("{}-{}".format(v2,v) in H)) or (v == v2):
                continue
              else:
                H.append("{}-{}".format(v,v2))
        return H
    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.A:
          if self.A[a].getV1() == self.A[a].getV2():
            return True
          else:
            continue
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        num = 0
        if V in self.N:
          for a in self.A:
            if (self.A[a].getV1() == V) and (self.A[a].getV2() == V):
              num+=2
            elif (self.A[a].getV1() == V) or (self.A[a].getV2() == V):
              num += 1
            else:
              continue
        else:
          raise VerticeInvalidoException("O vértice não existe no grafo")
        return num
    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for a in self.A:
          for b in self.A:
            if (self.A[a].getV1()== self.A[b].getV1()) and (self.A[a].getV2()== self.A[b].getV2()) and (a!=b):
              return True
        return False
    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V in self.N:
         Z = []
         for a in self.A:
           if (self.A[a].getV1()== V) or (self.A[a].getV2()== V):
              Z.append(a)
           else:
              continue
         return Z
        else:
          raise VerticeInvalidoException("Vértice não existe no grafo")
    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if (self.ha_laco == True) or (self.ha_paralelas() == True):
          return False
        else:
          s = 0
          k = (len(self.N)-1)
          for i in range(len(self.N)):
           s += k
           k -=1
          if len(self.A) != s:
            return False
          else:
            return True
    def dfs(self, V=''):
      Raiz = V
      x = 0
      Retorno = []
      Caminho = []
      Vertices = [Raiz]
      aux = [Raiz]
      dfs = MeuGrafo(deepcopy(self.N))
      self.procura_lado_n_dfs(Vertices,Caminho,Retorno,x,aux,Raiz)
      for arestas in Caminho:
        if arestas in self.A:
          dfs.adicionaAresta(arestas,self.A[arestas].getV1(),self.A[arestas].getV2())
      return dfs
    def procura_lado_n_dfs(self,Vertices,Caminho,Retorno,x,aux, Raiz= ''):
        As = self.arestas_sobre_vertice(Raiz)
        for a in As:
          if self.A[a].getV1() == Raiz:
            if self.A[a].getV2() not in Vertices:
               Vertices.append(self.A[a].getV2())
               aux.append(self.A[a].getV2())
               Caminho.append(a)
               Raiz = self.A[a].getV2()
               x+=1
               self.procura_lado_n_dfs(Vertices,Caminho, Retorno,x,aux,Raiz)
               x-=1
               aux.pop()
               Raiz = aux[x]
               continue
            else:
              if (a not in Caminho) and (a not in Retorno):
                Retorno.append(a)
                continue
              else:
                continue
          elif self.A[a].getV2() == Raiz:
            if self.A[a].getV1() not in Vertices:
               Vertices.append(self.A[a].getV1())
               aux.append(self.A[a].getV1())
               Caminho.append(a)
               Raiz = self.A[a].getV1()
               x+=1
               self.procura_lado_n_dfs(Vertices,Caminho, Retorno,x,aux,Raiz)
               x-=1
               aux.pop()
               Raiz = aux[x]
               continue
            else:
              if (a not in Caminho) and (a not in Retorno):
                Retorno.append(a)
                continue
              else:
                continue
        return
    def bfs(self, V=''):
      Raiz = V
      y = 0
      Retorno = []
      Caminho = []
      Vertices = [Raiz]
      aux1 = []
      aux2 = []
      bfs = MeuGrafo(deepcopy(self.N))
      self.procura_lado_n_bfs(Vertices,Caminho,Retorno,y,aux1,aux2,Raiz)
      for arestas in Caminho:
        if arestas in self.A:
          bfs.adicionaAresta(arestas,self.A[arestas].getV1(),self.A[arestas].getV2())
      return bfs
    def procura_lado_n_bfs(self,Vertices,Caminho,Retorno,y,aux1,aux2, Raiz= ''):
        Ar = self.arestas_sobre_vertice(Raiz)
        if y == 0 and aux1 == []:
          for a in Ar:
            y+=1
            if self.A[a].getV1() == Raiz:
              if self.A[a].getV2() not in Vertices:
                 Vertices.append(self.A[a].getV2())
                 aux1.append(self.A[a].getV2())
                 Caminho.append(a)
                 continue
              else:
                Retorno.append(a)
                y-=1
                continue
            elif self.A[a].getV2() == Raiz:
              if self.A[a].getV1() not in Vertices:
                 Vertices.append(self.A[a].getV1())
                 aux1.append(self.A[a].getV1())
                 Caminho.append(a)
                 continue
              else:
                Retorno.append(a)
                y-=1
                continue
          for x in range(y-1,-1,-1):
            Raiz = aux1[x]
            self.procura_lado_n_bfs(Vertices,Caminho,Retorno,y,aux1,aux2,Raiz)
          y=0
          while aux2 != []:
            aux1 = aux2[:]
            aux2 = []
            for n in aux1:
              Raiz = n
              self.procura_lado_n_bfs(Vertices,Caminho,Retorno,y,aux1,aux2,Raiz)
          else:
            return
        else:
          for a in Ar:
            if self.A[a].getV1() == Raiz:
                if self.A[a].getV2() not in Vertices:
                 Vertices.append(self.A[a].getV2())
                 aux2.append(self.A[a].getV2())
                 Caminho.append(a)
                 continue
                else:
                  Retorno.append(a)
                  continue
            elif self.A[a].getV2() == Raiz:
                if self.A[a].getV1() not in Vertices:
                 Vertices.append(self.A[a].getV1())
                 aux2.append(self.A[a].getV1())
                 Caminho.append(a)
                 continue
                else:
                  Retorno.append(a)
                  continue
          return
    def ha_ciclo(self):
      for V in self.N:
        Raiz = V
        x = 0
        Retorno = []
        Caminho = []
        Vertices = [Raiz]
        aux = [Raiz]
        self.procura_lado_n_dfs(Vertices,Caminho,Retorno,x,aux,Raiz)
        for r in Retorno:
          if (self.A[r].getV1()== V) or (self.A[r].getV2() ==V):
            Laço = [V]
            if (self.A[r].getV1()== V) and (self.A[r].getV2()== V):
              Laço.append(r)
              Laço.append(self.A[r].getV1())
              return Laço
            elif self.A[r].getV2()== V:
              Raiz = self.A[r].getV1()
              self.achar_caminho(Caminho,Laço,Raiz,V)
              Laço.append(r)
              Laço.append(self.A[r].getV2())
              return Laço
            else:
              Raiz = self.A[r].getV2()
              self.achar_caminho(Caminho,Laço,Raiz,V)
              Laço.append(r)
              Laço.append(self.A[r].getV1())
              return Laço
        continue
      return False
    def achar_caminho(self,Caminho,Laço,Raiz,V):
      As = self.arestas_sobre_vertice(Raiz)
      for a in As:
        if (a in Caminho):
          if self.A[a].getV1()== Raiz:
            Raiz = self.A[a].getV2()
            if Raiz != V:
              self.achar_caminho(Caminho,Laço,Raiz,V)
              if len(Laço)==1:
                continue
              else:
                Laço.append(a)
                Laço.append(self.A[a].getV1())
                return
            else:
              Laço.append(a)
              Laço.append(self.A[a].getV1())
              return
          else:
            Raiz = self.A[a].getV1()
            if Raiz != V:
              self.achar_caminho(Caminho,Laço,Raiz,V)
              if len(Laço)==1:
                continue
              else:
                Laço.append(a)
                Laço.append(self.A[a].getV2())
                return
            else:
              Laço.append(a)
              Laço.append(self.A[a].getV2())
              return
        else:
          continue
    def caminho(self,n):
        for V in self.N:
          CA = self.dfs(V)
          Ra = V
          Count = 0
          Vertices = [Ra]
          aux = [Ra]
          Passagem = [V]
          Caminho = []
          CA.achar_caminho_n(Ra,Count,Passagem,Vertices,aux,n,Caminho)
          if len(Passagem) == 1:
            continue
          else:
            return Passagem
        return False
    def achar_caminho_n(self,Ra,Count,Passagem,Vertices,aux,n,Caminho):
        As = self.arestas_sobre_vertice(Ra)
        for a in As:
            if len(Caminho)!= n:
                if self.A[a].getV1() == Ra:
                   if self.A[a].getV2() not in Vertices:
                      Vertices.append(self.A[a].getV2())
                      aux.append(self.A[a].getV2())
                      Passagem.append(a)
                      Caminho.append(a)
                      Ra = self.A[a].getV2()
                      Passagem.append(Ra)
                      Count += 1
                      self.achar_caminho_n(Ra,Count,Passagem,Vertices,aux,n,Caminho)
                      if len(Caminho)!= n:
                        Count -= 1
                        aux.pop()
                        Passagem.pop()
                        Passagem.pop()
                        Caminho.pop()
                        Ra = aux[Count]
                        continue
                      else:
                        return
                   else:
                      continue
                elif self.A[a].getV2() == Ra:
                   if self.A[a].getV1() not in Vertices:
                      Vertices.append(self.A[a].getV1())
                      aux.append(self.A[a].getV1())
                      Passagem.append(a)
                      Caminho.append(a)
                      Ra = self.A[a].getV1()
                      Passagem.append(Ra)
                      Count += 1
                      self.achar_caminho_n(Ra,Count,Passagem,Vertices,aux,n,Caminho)
                      if len(Caminho)!= n:
                        Count -= 1
                        aux.pop()
                        Passagem.pop()
                        Passagem.pop()
                        Caminho.pop()
                        Ra = aux[Count]
                        continue
                      else:
                        return
                else:
                    continue
            else:
                return
        return

    def conexo(self):
        Raiz = self.N[0]
        x = 0
        Retorno = []
        Caminho = []
        Vertices = [Raiz]
        aux = [Raiz]
        self.procura_lado_n_dfs(Vertices, Caminho, Retorno, x, aux, Raiz)
        for v in self.N:
            if v not in Vertices:
              return False
            else:
                continue
        return True
    def euler(self):
        Cont=0
        odd = []
        for V in self.N:
            if self.grau(V)%2==0:
                continue
            else:
                Cont+=1
                odd.append(V)
        if Cont == 0 and self.conexo():
            Gpast = MeuGrafo(deepcopy(self.N))
            for a in self.A:
                Gpast.adicionaAresta(a,self.A[a].getV1(),self.A[a].getV2())
            u = self.N[0]
            caminho = [u]
            Gpast.caminho_eu(u,caminho)
            return caminho
        elif Cont == 2 and self.conexo():
            Gpast = MeuGrafo(deepcopy(self.N))
            for a in self.A:
                Gpast.adicionaAresta(a, self.A[a].getV1(), self.A[a].getV2())
            u = odd[0]
            caminho = [u]
            Gpast.caminho_eu(u,caminho)
            return caminho
        else:
            return False
    def caminho_eu(self,u,caminho):
        As = self.arestas_sobre_vertice(u)
        for a in As:
            if len(As) == 0:
                return
            elif len(As)==1:
                if self.A[a].getV1() == u:
                    u = self.A[a].getV2()
                    caminho.append(a)
                    caminho.append(u)
                    self.removeAresta(a)
                    self.caminho_eu(u, caminho)
                    return
                else:
                    u = self.A[a].getV1()
                    caminho.append(a)
                    caminho.append(u)
                    self.removeAresta(a)
                    self.caminho_eu(u, caminho)
                    return
            else:
                if self.A[a].getV1() == u:
                    v = self.A[a].getV2()
                    h = a
                    self.removeAresta(a)
                    Raiz = v
                    x = 0
                    Retorno = []
                    Caminho = []
                    Vertices = [Raiz]
                    aux = [Raiz]
                    self.procura_lado_n_dfs(Vertices, Caminho, Retorno, x, aux, Raiz)
                    if u in Vertices:
                        u = v
                        caminho.append(a)
                        caminho.append(u)
                        self.caminho_eu(u, caminho)
                        return
                    else:
                        self.adicionaAresta(h,u,v)
                        continue
                else:
                    v = self.A[a].getV1()
                    h = a
                    self.removeAresta(a)
                    Raiz = v
                    x = 0
                    Retorno = []
                    Caminho = []
                    Vertices = [Raiz]
                    aux = [Raiz]
                    self.procura_lado_n_dfs(Vertices, Caminho, Retorno, x, aux, Raiz)
                    if u in Vertices:
                        u = v
                        caminho.append(a)
                        caminho.append(u)
                        self.caminho_eu(u, caminho)
                        return
                    else:
                        self.adicionaAresta(h, u, v)
                        continue
    def Prim(self):
      if (self.conexo() == False) or len(self.A) == 0:
        return False
      V =self.N.copy()
      E= self.A.copy()
      Jet = []
      P = []
      Comp = []
      Novo = MeuGrafo()
      aux = []
      As = []
      for a in E:
        if E[a].getV1() != E[a].getV2():
          Jet.append(E[a].getPeso())
          aux.append(a)
      indice = Jet.index(min(Jet))
      P.append(E[aux[indice]].getV1())
      Novo.adicionaVertice(P[0])
      V.pop(V.index(P[0]))
      while len(V)> 0:
         Ares = self.arestas_sobre_vertice(P[-1])
         for b in Ares:
           if (b not in As) and (b not in Novo.A) and (E[b].getV1() != E[b].getV2()) and (b in aux):
             As.append(b)
             Comp.append(Jet[aux.index(b)])
         c = As[Comp.index(min(Comp))]
         if (E[c].getV1()not in Novo.N) or (E[c].getV2() not in Novo.N):
           if E[c].getV1() not in P:
              P.append(E[c].getV1())
              V.remove(E[c].getV1())
           else:
              P.append(E[c].getV2())
              V.remove(E[c].getV2())
           Novo.adicionaVertice(P[-1])
           Novo.adicionaAresta(c,E[c].getV1(),E[c].getV2(),min(Comp))
           Comp.pop(As.index(c))
           As.remove(c)
           Jet.pop(aux.index(c))
           aux.pop(aux.index(c))
         else:
           Comp.pop(As.index(c))
           As.remove(c)
           Jet.pop(aux.index(c))
           aux.pop(aux.index(c))
      return Novo

    def Kruskal(self):
      if (self.conexo() == False) or len(self.A) == 0:
        return False
      V =self.N.copy()
      Pesos = []
      Arestas = []
      Novo = MeuGrafo()
      PesosL = []
      ArestasL = []
      Des = []
      Vr = []
      for a in self.A:
        if self.A[a].getV1() != self.A[a].getV2():
          PesosL.append(self.A[a].getPeso())
          ArestasL.append(a)
      while len(ArestasL) != 0:
          indice = PesosL.index(min(PesosL))
          Pesos.append(PesosL[indice])
          Arestas.append(ArestasL[indice])
          PesosL.pop(indice)
          ArestasL.pop(indice)
      while len(V)>0:
        C = Arestas[0]
        if (self.A[C].getV1() not in Novo.N) or (self.A[C].getV2() not in Novo.N):
          if self.A[C].getV2() in Novo.N:
            V.remove(self.A[C].getV1())
            Novo.adicionaVertice(self.A[C].getV1())
          elif self.A[C].getV1() in Novo.N:
            V.remove(self.A[C].getV2())
            Novo.adicionaVertice(self.A[C].getV2())
          else:
            V.remove(self.A[C].getV1())
            V.remove(self.A[C].getV2())
            Novo.adicionaVertice(self.A[C].getV1())
            Novo.adicionaVertice(self.A[C].getV2())
          Novo.adicionaAresta(C,self.A[C].getV1(),self.A[C].getV2(),Pesos[0])
          Pesos.pop(0)
          Arestas.pop(0)
        else:
           Pesos.pop(0)
           Arestas.pop(0)
      Des = Novo.desconexo()
      while Des!= False:
        self.Notdes(Novo,Arestas,Pesos,ArestasL,PesosL,Vr,Des)
        Pesos = []
        Arestas = []
        PesosL = []
        ArestasL = []
        Des = []
        Vr = []
        Des = Novo.desconexo()
      return Novo

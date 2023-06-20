from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''

        arestas = set()
        for a in self.arestas:
            arestaAtual = self.arestas[a]
            vertices = f'{arestaAtual.v1}-{arestaAtual.v2}'
            arestas.add(vertices)

        vna = set()
        for x in range(len(self.vertices)):
            for y in range(x+1, len(self.vertices)):
                novaAresta = f'{self.vertices[x]}-{self.vertices[y]}'

                if novaAresta not in arestas and novaAresta[::-1] not in arestas:
                    vna.add(novaAresta)

        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        arestas = self.arestas

        for a in arestas:
            if arestas[a].v1 == arestas[a].v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo.")

        arestas = self.arestas
        grau = 0

        for a in arestas:
            if arestas[a].v1.rotulo == V or arestas[a].v2.rotulo == V:
                grau += 1
            if arestas[a].v1 == arestas[a].v2 or arestas[a].v2 == arestas[a].v1:
                grau += 1

        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        arestas = self.arestas
        for x in arestas:
            for y in arestas:
                if x != y:
                    if(arestas[x].v1 == arestas[y].v1) and (arestas[x].v2 == arestas[y].v2):
                        return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        arestas = self.arestas
        asv = set()

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo.")

        for a in arestas:
            if arestas[a].v1.rotulo == V or arestas[a].v2.rotulo == V:
                asv.add(a)

        return asv

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        vertices = self.vertices
        grauEsperado = len(self.vertices)-1

        for v in vertices:
            if self.grau(v.rotulo) != grauEsperado:
                return False

        return True

    def vertice_oposto(self, vertice, aresta):
        if aresta.v1.rotulo == vertice:
            return aresta.v2.rotulo
        else:
            return aresta.v1.rotulo

    def dfs(self, V = ""):
        arvore_dfs = MeuGrafo()

        return self.dfs_aux(arvore_dfs, V)

    def dfs_aux(self, arvore_dfs, vertice):

        if not arvore_dfs.existe_rotulo_vertice(vertice):
            arvore_dfs.adiciona_vertice(vertice)

        arestas = self.arestas_sobre_vertice(vertice)
        arestas = list(arestas)
        arestas.sort()

        for a in arestas:

            if self.arestas[a].v1.rotulo == vertice:
                v = self.arestas[a].v2.rotulo
            else:
                v = self.arestas[a].v1.rotulo

            if not arvore_dfs.existe_rotulo_vertice(v):
                arvore_dfs.adiciona_vertice(v)
                arvore_dfs.adiciona_aresta(self.arestas[a])

                self.dfs_aux(arvore_dfs, v)

        return arvore_dfs

    def bfs(self, V = ""):
        arvore_bfs = MeuGrafo()

        return self.bfs_aux(arvore_bfs, V)

    def bfs_aux(self, arvore_bfs, vertice):

        if not arvore_bfs.existe_rotulo_vertice(vertice):
            arvore_bfs.adiciona_vertice(vertice)

        arestas = self.arestas_sobre_vertice(vertice)
        arestas = list(arestas)
        arestas.sort()

        for a in arestas:
            if self.arestas[a].v1.rotulo == vertice:
                v = self.arestas[a].v2.rotulo
            else:
                v = self.arestas[a].v1.rotulo

            if not arvore_bfs.existe_rotulo_vertice(v):
                arvore_bfs.adiciona_vertice(v)
                arvore_bfs.adiciona_aresta(self.arestas[a])

        for a in arestas:
            if self.arestas[a].v1.rotulo == vertice:
                v = self.arestas[a].v2.rotulo
            else:
                v = self.arestas[a].v1.rotulo

            self.dfs_aux(arvore_bfs, v)

        return arvore_bfs


    def conexo(self):
        '''
        Verifica se o grafo é conexo.
        :return: Um valor booleano que indica se o grafo é conexo
        '''
        qtd_vertices = len(self.vertices)
        vertice = self.vertices[0]
        vertice = str(vertice)
        arvore = self.dfs(vertice)
        qtd_Vconexo = len(arvore.vertices)

        if qtd_Vconexo == qtd_vertices:
            return True
        else:
            return False

    def prim(self):
        mst_prim = MeuGrafo()
        arestas_ordenadas = sorted(self.arestas, key=lambda a: self.arestas[a].peso)
        primeira_aresta = arestas_ordenadas[0]
        proximo_vertice = self.arestas[primeira_aresta].v1.rotulo
        mst_prim.adiciona_vertice(proximo_vertice)

        while len(mst_prim.vertices) < len(self.vertices):
            arestas_sobre_vertice = self.arestas_sobre_vertice(proximo_vertice)
            menor_peso = float('inf')
            menor_aresta = ''

            for a in arestas_sobre_vertice:
                if self.arestas[a].peso <= menor_peso:
                    if not mst_prim.existe_rotulo_vertice(self.vertice_oposto(proximo_vertice, self.arestas[a])):
                        menor_aresta = self.arestas[a]
                        menor_peso = self.arestas[a].peso

            proximo_vertice = self.vertice_oposto(proximo_vertice, menor_aresta)

            if not mst_prim.existe_rotulo_vertice(proximo_vertice):
                mst_prim.adiciona_vertice(proximo_vertice)
                mst_prim.adiciona_aresta(menor_aresta)

        return mst_prim

    def Kruskall(self):
        mst = MeuGrafo()
        prioridade = self.bucket_sort()

        for v in self.vertices:
            mst.adiciona_vertice(v.rotulo)

        for i in range(len(prioridade)):
            for a in prioridade[i]:
                aresta = self.arestas[a]
                dfs_mst = mst.dfs(aresta.v1.rotulo)

                if dfs_mst.existe_rotulo_vertice(aresta.v1.rotulo) and dfs_mst.existe_rotulo_vertice(aresta.v2.rotulo):
                    pass
                else:
                    mst.adiciona_aresta(aresta)

        return mst

    def bucket_sort(self):
        pesos_dict = {}
        for a in self.arestas:
            peso = self.arestas[a].peso
            if peso not in pesos_dict:
                pesos_dict[peso] = []
            pesos_dict[peso].append(a)

        bucket = [pesos_dict[peso] for peso in sorted(pesos_dict)]

        return bucket



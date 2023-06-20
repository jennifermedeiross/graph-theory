from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        v = self.get_vertice(V)
        index = self.indice_do_vertice(v)
        arestas = list()

        for c in range(len(self.matriz)):
            for aresta in self.matriz[index][c]:
                arestas.append(self.matriz[index][c][aresta])
        for c in range(len(self.matriz)):
            for aresta in self.matriz[c][index]:
                arestas.append(self.matriz[c][index][aresta])
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        E = list()
        vertices = self.vertices
        ordem = len(vertices)

        #Copiando matriz para E
        for i in range(ordem):
            E.append(list())
            for j in range(ordem):
                if len(self.matriz[i][j]) != 0:
                    E[i].append(1)
                else:
                    E[i].append(0)

        for i in range(ordem):
            for j in range(ordem):
                if E[j][i] == 1:
                    for k in range(ordem):
                        E[j][k] = max(E[j][k], E[i][k])

        return E

    def dijkstra(self, U, V):
        vertices = self.vertices

        w = U #Vértice em análise
        beta = {str(v): float('inf') for v in vertices} #Peso do menor caminho
        gama = {str(v): 0 for v in vertices} #Marcador do vértice
        pi = {str(v): 0 for v in vertices} #Precessor de w
        cDijkstra = []

        beta[U] = 0
        gama[U] = 1

        while True:
            if w == V:
                break
            for a in self.arestas_sobre_vertice(w):
                if w == a.v1.rotulo:
                    vc = a.v2.rotulo
                else:
                    vc = w

                pesoAresta = a.peso
                if gama[vc] == 0 and beta[vc] > (beta[w] + pesoAresta):
                    beta[vc] = beta[w] + pesoAresta
                    pi[vc] = w

            menor = float('inf')
            for i in beta:
                if beta[i] < menor and gama[i] == 0:
                    menor = beta[i]

            for key, value in beta.items():
                if value == menor:
                    w = key
                    break

            gama[w] = 1

        while True:
            cDijkstra.append(V)
            if V == U:
                return cDijkstra
            V = pi[V]

    def khan(self):
        copia = deepcopy(self)
        ordem_topologica = []

        while copia.vertices:
            nodos_fonte = []
            for i in range(len(copia.vertices)):
                vertice = copia.vertices[i]
                if not any(copia.matriz[j][i] for j in range(len(copia.vertices))): #função python que verifica se algum valor dentro da iteração é verdadeira, mas negada
                    nodos_fonte.append(vertice.rotulo)

            for nodo in nodos_fonte:
                arestas = copia.arestas_sobre_vertice(nodo)
                for aresta in arestas:
                    copia.remove_aresta(aresta.rotulo)
                copia.remove_vertice(nodo)
                ordem_topologica.append(nodo)

        return ordem_topologica

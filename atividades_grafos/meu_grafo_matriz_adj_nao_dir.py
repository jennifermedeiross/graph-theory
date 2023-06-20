from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''

        vertices = self.vertices
        vna = []

        for c in range(len(vertices)):
            for i in range(len(vertices)):
                if c != i and len(self.matriz[c][i]) == 0:
                    if not f'{vertices[i]}-{vertices[c]}' in vna:
                        vna.append(f'{vertices[c]}-{vertices[i]}')

        vna = set(vna)

        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        vertices = self.vertices
        for c in range(len(vertices)):
            if len(self.matriz[c][c]) > 0:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f"Vértice {V} não existe no grafo")

        grau = 0
        indexVertice = self.vertices.index(self.get_vertice(V))
        vertices = self.vertices

        for c in range(len(vertices)):
            if indexVertice == c and len(self.matriz[indexVertice][c]) > 0:
                grau += 2 * len(self.matriz[indexVertice][c])
            else:
                if len(self.matriz[indexVertice][c]) > 0:
                    grau += len(self.matriz[indexVertice][c])
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        vertices = self.vertices

        for c in range(len(vertices)):
            for i in range(len(vertices)):
                if len(self.matriz[c][i]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("Vértice {} não existe no grafo".format(V))

        v_obj = self.get_vertice(V)
        i_v = self.indice_do_vertice(v_obj)
        arestas = set()
        for j in range(len(self.vertices)):
            for a in self.matriz[i_v][j]:
                arestas.add(a)
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        vertices = self.vertices
        if self.ha_laco():
            return False
        for c in range(len(vertices)):
            for i in range(len(vertices)):
                if len(self.matriz[c][i]) < 1 and c != i:
                    return False
        return True

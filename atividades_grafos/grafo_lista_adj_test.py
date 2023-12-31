import unittest
from meu_grafo_lista_adj import *
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # Versão DFS de g_p

        self.g_p_dfs = MeuGrafo()
        self.g_p_dfs.adiciona_vertice("J")
        self.g_p_dfs.adiciona_vertice("C")
        self.g_p_dfs.adiciona_vertice("P")
        self.g_p_dfs.adiciona_vertice("E")
        self.g_p_dfs.adiciona_vertice("M")
        self.g_p_dfs.adiciona_vertice("T")
        self.g_p_dfs.adiciona_vertice("Z")
        self.g_p_dfs.adiciona_aresta('a1', 'J', 'C')
        self.g_p_dfs.adiciona_aresta('a4', 'C', 'P')
        self.g_p_dfs.adiciona_aresta('a2', 'C', 'E')
        self.g_p_dfs.adiciona_aresta('a6', 'C', 'T')
        self.g_p_dfs.adiciona_aresta('a8', 'M', 'T')
        self.g_p_dfs.adiciona_aresta('a9', 'T', 'Z')

        # Versão BFS de g_p
        self.g_p_bfs = MeuGrafo()
        self.g_p_bfs.adiciona_vertice("J")
        self.g_p_bfs.adiciona_vertice("C")
        self.g_p_bfs.adiciona_vertice("P")
        self.g_p_bfs.adiciona_vertice("E")
        self.g_p_bfs.adiciona_vertice("M")
        self.g_p_bfs.adiciona_vertice("T")
        self.g_p_bfs.adiciona_vertice("Z")
        self.g_p_bfs.adiciona_aresta('a1', 'J', 'C')
        self.g_p_bfs.adiciona_aresta('a2', 'C', 'E')
        self.g_p_bfs.adiciona_aresta('a4', 'P', 'C')
        self.g_p_bfs.adiciona_aresta('a6', 'T', 'C')
        self.g_p_bfs.adiciona_aresta('a8', 'M', 'T')
        self.g_p_bfs.adiciona_aresta('a9', 'T', 'Z')


        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        #Versão DFS de g_p4
        self.g_p4_dfs = MeuGrafo()
        self.g_p4_dfs.adiciona_vertice("J")
        self.g_p4_dfs.adiciona_vertice("C")
        self.g_p4_dfs.adiciona_vertice("E")
        self.g_p4_dfs.adiciona_vertice("P")
        self.g_p4_dfs.adiciona_vertice("M")
        self.g_p4_dfs.adiciona_vertice("T")
        self.g_p4_dfs.adiciona_vertice("Z")
        self.g_p4_dfs.adiciona_aresta('a1', 'J', 'C')
        self.g_p4_dfs.adiciona_aresta('a3', 'C', 'E')
        self.g_p4_dfs.adiciona_aresta('a4', 'P', 'C')
        self.g_p4_dfs.adiciona_aresta('a6', 'T', 'C')
        self.g_p4_dfs.adiciona_aresta('a8', 'M', 'T')
        self.g_p4_dfs.adiciona_aresta('a9', 'T', 'Z')

        # Versão BFS de g_p4
        self.g_p4_bfs = MeuGrafo()
        self.g_p4_bfs.adiciona_vertice("J")
        self.g_p4_bfs.adiciona_vertice("C")
        self.g_p4_bfs.adiciona_vertice("E")
        self.g_p4_bfs.adiciona_vertice("P")
        self.g_p4_bfs.adiciona_vertice("M")
        self.g_p4_bfs.adiciona_vertice("T")
        self.g_p4_bfs.adiciona_vertice("Z")
        self.g_p4_bfs.adiciona_aresta('a1', 'J', 'C')
        self.g_p4_bfs.adiciona_aresta('a2', 'J', 'E')
        self.g_p4_bfs.adiciona_aresta('a4', 'P', 'C')
        self.g_p4_bfs.adiciona_aresta('a6', 'T', 'C')
        self.g_p4_bfs.adiciona_aresta('a8', 'M', 'T')
        self.g_p4_bfs.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        #Versão DFS de g_c
        self.g_c_dfs = MeuGrafo()
        self.g_c_dfs.adiciona_vertice("J")
        self.g_c_dfs.adiciona_vertice("C")
        self.g_c_dfs.adiciona_vertice("E")
        self.g_c_dfs.adiciona_vertice("P")
        self.g_c_dfs.adiciona_aresta('a1', 'J', 'C')
        self.g_c_dfs.adiciona_aresta('a4', 'E', 'C')
        self.g_c_dfs.adiciona_aresta('a6', 'P', 'E')

        #Versão BFS de g_c
        self.g_c_bfs = MeuGrafo()
        self.g_c_bfs.adiciona_vertice("J")
        self.g_c_bfs.adiciona_vertice("C")
        self.g_c_bfs.adiciona_vertice("E")
        self.g_c_bfs.adiciona_vertice("P")
        self.g_c_bfs.adiciona_aresta('a1', 'J', 'C')
        self.g_c_bfs.adiciona_aresta('a2', 'J', 'E')
        self.g_c_bfs.adiciona_aresta('a3', 'J', 'P')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo()
        self.g_d2.adiciona_vertice("A")
        self.g_d2.adiciona_vertice("B")
        self.g_d2.adiciona_vertice("C")
        self.g_d2.adiciona_vertice("D")

        # Grafos teste

        self.g_pe = MeuGrafo()
        self.g_pe.adiciona_vertice("P")
        self.g_pe.adiciona_vertice("S")
        self.g_pe.adiciona_vertice("ALA")
        self.g_pe.adiciona_vertice("V")
        self.g_pe.adiciona_vertice("BJ")
        self.g_pe.adiciona_vertice("SBU")
        self.g_pe.adiciona_vertice("GUS")
        self.g_pe.adiciona_vertice("L")
        self.g_pe.adiciona_vertice("SC")
        self.g_pe.adiciona_vertice("AG")
        self.g_pe.adiciona_vertice("C")
        self.g_pe.adiciona_aresta("a1", "P", "S")
        self.g_pe.adiciona_aresta("a2", "S", "BJ")
        self.g_pe.adiciona_aresta("a3", "BJ", "SBU")
        self.g_pe.adiciona_aresta("a4", "SBU", "GUS")
        self.g_pe.adiciona_aresta("a5", "GUS", "V")
        self.g_pe.adiciona_aresta("a6", "V", "ALA")
        self.g_pe.adiciona_aresta("a7", "ALA", "P")
        self.g_pe.adiciona_aresta("a8", "GUS", "L")
        self.g_pe.adiciona_aresta("a9", "L", "SBU")

        #Versão DFS de g_pe
        self.g_pe_dfs = MeuGrafo()
        self.g_pe_dfs.adiciona_vertice("P")
        self.g_pe_dfs.adiciona_vertice("S")
        self.g_pe_dfs.adiciona_vertice("ALA")
        self.g_pe_dfs.adiciona_vertice("V")
        self.g_pe_dfs.adiciona_vertice("BJ")
        self.g_pe_dfs.adiciona_vertice("SBU")
        self.g_pe_dfs.adiciona_vertice("GUS")
        self.g_pe_dfs.adiciona_vertice("L")
        self.g_pe_dfs.adiciona_aresta("a1", "P", "S")
        self.g_pe_dfs.adiciona_aresta("a2", "S", "BJ")
        self.g_pe_dfs.adiciona_aresta("a3", "BJ", "SBU")
        self.g_pe_dfs.adiciona_aresta("a4", "SBU", "GUS")
        self.g_pe_dfs.adiciona_aresta("a5", "GUS", "V")
        self.g_pe_dfs.adiciona_aresta("a6", "V", "ALA")
        self.g_pe_dfs.adiciona_aresta("a8", "GUS", "L")

        #Versão BFS do g_pe
        self.g_pe_bfs = MeuGrafo()
        self.g_pe_bfs.adiciona_vertice("P")
        self.g_pe_bfs.adiciona_vertice("S")
        self.g_pe_bfs.adiciona_vertice("ALA")
        self.g_pe_bfs.adiciona_vertice("V")
        self.g_pe_bfs.adiciona_vertice("BJ")
        self.g_pe_bfs.adiciona_vertice("SBU")
        self.g_pe_bfs.adiciona_vertice("GUS")
        self.g_pe_bfs.adiciona_vertice("L")
        self.g_pe_bfs.adiciona_aresta("a1", "P", "S")
        self.g_pe_bfs.adiciona_aresta("a7", "ALA", "P")
        self.g_pe_bfs.adiciona_aresta("a2", "S", "BJ")
        self.g_pe_bfs.adiciona_aresta("a3", "BJ", "SBU")
        self.g_pe_bfs.adiciona_aresta("a4", "SBU", "GUS")
        self.g_pe_bfs.adiciona_aresta("a5", "GUS", "V")
        self.g_pe_bfs.adiciona_aresta("a8", "GUS", "L")


        self.g_laco = MeuGrafo()
        self.g_laco.adiciona_vertice("K")
        self.g_laco.adiciona_vertice("L")
        self.g_laco.adiciona_vertice("M")
        self.g_laco.adiciona_vertice("N")
        self.g_laco.adiciona_vertice("COISA")
        self.g_laco.adiciona_aresta("KCOISA", "K", "COISA")
        self.g_laco.adiciona_aresta("KL", "K", "L")
        self.g_laco.adiciona_aresta("lm", "L", "M")
        self.g_laco.adiciona_aresta("a1", "K", "COISA")
        self.g_laco.adiciona_aresta("a2", "N", "L")

        #Versão DFS de g_laco
        self.g_laco_dfs = MeuGrafo()
        self.g_laco_dfs.adiciona_vertice("K")
        self.g_laco_dfs.adiciona_vertice("L")
        self.g_laco_dfs.adiciona_vertice("M")
        self.g_laco_dfs.adiciona_vertice("N")
        self.g_laco_dfs.adiciona_vertice("COISA")
        self.g_laco_dfs.adiciona_aresta("KCOISA", "K", "COISA")
        self.g_laco_dfs.adiciona_aresta("KL", "K", "L")
        self.g_laco_dfs.adiciona_aresta("lm", "L", "M")
        self.g_laco_dfs.adiciona_aresta("a2", "N", "L")

        # Versão BFS de g_laco
        self.g_laco_bfs = MeuGrafo()
        self.g_laco_bfs.adiciona_vertice("K")
        self.g_laco_bfs.adiciona_vertice("L")
        self.g_laco_bfs.adiciona_vertice("M")
        self.g_laco_bfs.adiciona_vertice("N")
        self.g_laco_bfs.adiciona_vertice("COISA")
        self.g_laco_bfs.adiciona_aresta("KCOISA", "K", "COISA")
        self.g_laco_bfs.adiciona_aresta("KL", "K", "L")
        self.g_laco_bfs.adiciona_aresta("lm", "L", "M")
        self.g_laco_bfs.adiciona_aresta("a2", "N", "L")


        self.g_teste1 = MeuGrafo()
        self.g_teste1.adiciona_vertice("A")
        self.g_teste1.adiciona_vertice("B")
        self.g_teste1.adiciona_vertice("C")
        self.g_teste1.adiciona_vertice("D")
        self.g_teste1.adiciona_vertice("E")
        self.g_teste1.adiciona_vertice("F")
        self.g_teste1.adiciona_vertice("G")
        self.g_teste1.adiciona_aresta("a1", "A", "B")
        self.g_teste1.adiciona_aresta("a2", "A", "C")
        self.g_teste1.adiciona_aresta("a3", "B", "G")
        self.g_teste1.adiciona_aresta("a4", "C", "D")
        self.g_teste1.adiciona_aresta("a5", "C", "E")
        self.g_teste1.adiciona_aresta("a6", "C", "F")
        self.g_teste1.adiciona_aresta("a7", "E", "F")

        #Versão DFS de g_teste1
        self.g_teste1_dfs = MeuGrafo()
        self.g_teste1_dfs.adiciona_vertice("A")
        self.g_teste1_dfs.adiciona_vertice("B")
        self.g_teste1_dfs.adiciona_vertice("C")
        self.g_teste1_dfs.adiciona_vertice("D")
        self.g_teste1_dfs.adiciona_vertice("E")
        self.g_teste1_dfs.adiciona_vertice("F")
        self.g_teste1_dfs.adiciona_vertice("G")
        self.g_teste1_dfs.adiciona_aresta("a1", "A", "B")
        self.g_teste1_dfs.adiciona_aresta("a3", "B", "G")
        self.g_teste1_dfs.adiciona_aresta("a2", "A", "C")
        self.g_teste1_dfs.adiciona_aresta("a4", "C", "D")
        self.g_teste1_dfs.adiciona_aresta("a5", "C", "E")
        self.g_teste1_dfs.adiciona_aresta("a7", "E", "F")

        #Versão BFS de g_teste1
        self.g_teste1_bfs = MeuGrafo()
        self.g_teste1_bfs.adiciona_vertice("A")
        self.g_teste1_bfs.adiciona_vertice("B")
        self.g_teste1_bfs.adiciona_vertice("C")
        self.g_teste1_bfs.adiciona_vertice("D")
        self.g_teste1_bfs.adiciona_vertice("E")
        self.g_teste1_bfs.adiciona_vertice("F")
        self.g_teste1_bfs.adiciona_vertice("G")
        self.g_teste1_bfs.adiciona_aresta("a1", "A", "B")
        self.g_teste1_bfs.adiciona_aresta("a2", "A", "C")
        self.g_teste1_bfs.adiciona_aresta("a3", "B", "G")
        self.g_teste1_bfs.adiciona_aresta("a4", "C", "D")
        self.g_teste1_bfs.adiciona_aresta("a5", "C", "E")
        self.g_teste1_bfs.adiciona_aresta("a7", "E", "F")

        # MST

        self.g_grafo1 = MeuGrafo()
        self.g_grafo1.adiciona_vertice("1")
        self.g_grafo1.adiciona_vertice("2")
        self.g_grafo1.adiciona_vertice("3")
        self.g_grafo1.adiciona_vertice("4")
        self.g_grafo1.adiciona_vertice("5")
        self.g_grafo1.adiciona_vertice("6")
        self.g_grafo1.adiciona_vertice("7")
        self.g_grafo1.adiciona_vertice("8")
        self.g_grafo1.adiciona_vertice("9")
        self.g_grafo1.adiciona_aresta('a1', '1', '2', 1)
        self.g_grafo1.adiciona_aresta('a2', '2', '4', 10)
        self.g_grafo1.adiciona_aresta('a3', '3', '2', 8)
        self.g_grafo1.adiciona_aresta('a4', '2', '3', 8)
        self.g_grafo1.adiciona_aresta('a5', '2', '4', 2)
        self.g_grafo1.adiciona_aresta('a6', '2', '6', 3)
        self.g_grafo1.adiciona_aresta('a7', '2', '5', 1)
        self.g_grafo1.adiciona_aresta('a8', '5', '6', 2)
        self.g_grafo1.adiciona_aresta('a9', '8', '6', 1)
        self.g_grafo1.adiciona_aresta('a10', '7', '6', 3)
        self.g_grafo1.adiciona_aresta('a11', '8', '7', 2)
        self.g_grafo1.adiciona_aresta('a12', '8', '9', 10)

        self.g_grafo2 = MeuGrafo()
        self.g_grafo2.adiciona_vertice("A")
        self.g_grafo2.adiciona_vertice("B")
        self.g_grafo2.adiciona_vertice("C")
        self.g_grafo2.adiciona_vertice("D")
        self.g_grafo2.adiciona_vertice("E")
        self.g_grafo2.adiciona_vertice("F")
        self.g_grafo2.adiciona_vertice("G")
        self.g_grafo2.adiciona_vertice("H")
        self.g_grafo2.adiciona_vertice("I")
        self.g_grafo2.adiciona_vertice("J")
        self.g_grafo2.adiciona_vertice("K")
        self.g_grafo2.adiciona_aresta("1", "A", "B", 10)
        self.g_grafo2.adiciona_aresta("2", "A", "G", 10)
        self.g_grafo2.adiciona_aresta("3", "A", "J", 3)
        self.g_grafo2.adiciona_aresta("4", "K", "G", 1)
        self.g_grafo2.adiciona_aresta("5", "K", "J", 6)
        self.g_grafo2.adiciona_aresta("6", "J", "G", 7)
        self.g_grafo2.adiciona_aresta("7", "J", "I", 5)
        self.g_grafo2.adiciona_aresta("8", "I", "G", 1)
        self.g_grafo2.adiciona_aresta("9", "G", "H", 1)
        self.g_grafo2.adiciona_aresta("10", "H", "F", 6)
        self.g_grafo2.adiciona_aresta("11", "F", "B", 10)
        self.g_grafo2.adiciona_aresta("12", "B", "G", 12)
        self.g_grafo2.adiciona_aresta("13", "B", "C", 2)
        self.g_grafo2.adiciona_aresta("14", "C", "D", 4)
        self.g_grafo2.adiciona_aresta("15", "D", "E", 3)
        self.g_grafo2.adiciona_aresta("16", "D", "B", 1)
        self.g_grafo2.adiciona_aresta("17", "E", "B", 1)

        self.g_grafo3 = MeuGrafo()
        self.g_grafo3.adiciona_vertice("A")
        self.g_grafo3.adiciona_vertice("B")
        self.g_grafo3.adiciona_vertice("C")
        self.g_grafo3.adiciona_vertice("D")
        self.g_grafo3.adiciona_vertice("E")
        self.g_grafo3.adiciona_vertice("F")
        self.g_grafo3.adiciona_vertice("G")
        self.g_grafo3.adiciona_aresta("a1", "A", "B", 1)
        self.g_grafo3.adiciona_aresta("a2", "B", "C", 1)
        self.g_grafo3.adiciona_aresta("a3", "B", "F", 3)
        self.g_grafo3.adiciona_aresta("a4", "C", "D", 1)
        self.g_grafo3.adiciona_aresta("a5", "C", "E", 2)
        self.g_grafo3.adiciona_aresta("a6", "D", "E", 3)
        self.g_grafo3.adiciona_aresta("a7", "E", "G", 2)
        self.g_grafo3.adiciona_aresta("a8", "F", "G", 1)

        self.g_grafo5 = MeuGrafo()
        self.g_grafo5.adiciona_vertice("0")
        self.g_grafo5.adiciona_vertice("1")
        self.g_grafo5.adiciona_vertice("2")
        self.g_grafo5.adiciona_vertice("3")
        self.g_grafo5.adiciona_vertice("4")
        self.g_grafo5.adiciona_vertice("5")
        self.g_grafo5.adiciona_vertice("6")
        self.g_grafo5.adiciona_vertice("7")
        self.g_grafo5.adiciona_vertice("8")
        self.g_grafo5.adiciona_aresta("q1", "0", "1", 4)
        self.g_grafo5.adiciona_aresta("q2", "0", "7", 8)
        self.g_grafo5.adiciona_aresta("q3", "1", "2", 8)
        self.g_grafo5.adiciona_aresta("q4", "1", "7", 11)
        self.g_grafo5.adiciona_aresta("q5", "2", "3", 7)
        self.g_grafo5.adiciona_aresta("q6", "2", "5", 4)
        self.g_grafo5.adiciona_aresta("q7", "2", "8", 2)
        self.g_grafo5.adiciona_aresta("q8", "3", "4", 9)
        self.g_grafo5.adiciona_aresta("q9", "3", "5", 14)
        self.g_grafo5.adiciona_aresta("q10", "4", "5", 10)
        self.g_grafo5.adiciona_aresta("q11", "5", "6", 2)
        self.g_grafo5.adiciona_aresta("q12", "6", "7", 1)
        self.g_grafo5.adiciona_aresta("q13", "6", "8", 6)
        self.g_grafo5.adiciona_aresta("q14", "7", "8", 7)

        self.g_grafo1_krsk = MeuGrafo()
        self.g_grafo1_krsk.adiciona_vertice("1")
        self.g_grafo1_krsk.adiciona_vertice("2")
        self.g_grafo1_krsk.adiciona_vertice("3")
        self.g_grafo1_krsk.adiciona_vertice("4")
        self.g_grafo1_krsk.adiciona_vertice("5")
        self.g_grafo1_krsk.adiciona_vertice("6")
        self.g_grafo1_krsk.adiciona_vertice("7")
        self.g_grafo1_krsk.adiciona_vertice("8")
        self.g_grafo1_krsk.adiciona_vertice("9")
        self.g_grafo1_krsk.adiciona_aresta('a1', '1', '2', 1)
        self.g_grafo1_krsk.adiciona_aresta('a7', '2', '5', 1)
        self.g_grafo1_krsk.adiciona_aresta('a9', '8', '6', 1)
        self.g_grafo1_krsk.adiciona_aresta('a11', '8', '7', 2)
        self.g_grafo1_krsk.adiciona_aresta('a5', '2', '4', 2)
        self.g_grafo1_krsk.adiciona_aresta('a8', '5', '6', 2)
        self.g_grafo1_krsk.adiciona_aresta('a3', '3', '2', 8)
        self.g_grafo1_krsk.adiciona_aresta('a12', '8', '9', 10)

        self.g_grafo2_krsk = MeuGrafo()
        self.g_grafo2_krsk.adiciona_vertice("D")
        self.g_grafo2_krsk.adiciona_vertice("B")
        self.g_grafo2_krsk.adiciona_vertice("E")
        self.g_grafo2_krsk.adiciona_vertice("K")
        self.g_grafo2_krsk.adiciona_vertice("G")
        self.g_grafo2_krsk.adiciona_vertice("I")
        self.g_grafo2_krsk.adiciona_vertice("H")
        self.g_grafo2_krsk.adiciona_vertice("C")
        self.g_grafo2_krsk.adiciona_vertice("A")
        self.g_grafo2_krsk.adiciona_vertice("J")
        self.g_grafo2_krsk.adiciona_vertice("F")
        self.g_grafo2_krsk.adiciona_aresta('16', 'D', 'B', 1)
        self.g_grafo2_krsk.adiciona_aresta('17', 'E', 'B', 1)
        self.g_grafo2_krsk.adiciona_aresta('4', 'K', 'G', 1)
        self.g_grafo2_krsk.adiciona_aresta('8', 'I', 'G', 1)
        self.g_grafo2_krsk.adiciona_aresta('9', 'G', 'H', 1)
        self.g_grafo2_krsk.adiciona_aresta('13', 'B', 'C', 2)
        self.g_grafo2_krsk.adiciona_aresta('3', 'A', 'J', 3)
        self.g_grafo2_krsk.adiciona_aresta('7', 'J', 'I', 5)
        self.g_grafo2_krsk.adiciona_aresta('10', 'H', 'F', 6)
        self.g_grafo2_krsk.adiciona_aresta('1', 'A', 'B', 10)

        self.g_grafo3_krsk = MeuGrafo()
        self.g_grafo3_krsk.adiciona_vertice("A")
        self.g_grafo3_krsk.adiciona_vertice("B")
        self.g_grafo3_krsk.adiciona_vertice("C")
        self.g_grafo3_krsk.adiciona_vertice("D")
        self.g_grafo3_krsk.adiciona_vertice("E")
        self.g_grafo3_krsk.adiciona_vertice("F")
        self.g_grafo3_krsk.adiciona_vertice("G")
        self.g_grafo3_krsk.adiciona_aresta('a1', 'A', 'B', 1)
        self.g_grafo3_krsk.adiciona_aresta('a2', 'B', 'C', 1)
        self.g_grafo3_krsk.adiciona_aresta('a4', 'C', 'D', 1)
        self.g_grafo3_krsk.adiciona_aresta('a8', 'F', 'G', 1)
        self.g_grafo3_krsk.adiciona_aresta('a5', 'C', 'E', 2)
        self.g_grafo3_krsk.adiciona_aresta('a7', 'E', 'G', 2)

        self.g_grafo5_krsk = MeuGrafo()
        self.g_grafo5_krsk.adiciona_vertice("6")
        self.g_grafo5_krsk.adiciona_vertice("7")
        self.g_grafo5_krsk.adiciona_vertice("5")
        self.g_grafo5_krsk.adiciona_vertice("2")
        self.g_grafo5_krsk.adiciona_vertice("8")
        self.g_grafo5_krsk.adiciona_vertice("3")
        self.g_grafo5_krsk.adiciona_vertice("0")
        self.g_grafo5_krsk.adiciona_vertice("1")
        self.g_grafo5_krsk.adiciona_vertice("4")
        self.g_grafo5_krsk.adiciona_aresta('q12', '6', '7', 1)
        self.g_grafo5_krsk.adiciona_aresta('q11', '5', '6', 2)
        self.g_grafo5_krsk.adiciona_aresta('q6', '2', '5', 4)
        self.g_grafo5_krsk.adiciona_aresta('q7', '2', '8', 2)
        self.g_grafo5_krsk.adiciona_aresta('q5', '2', '3', 7)
        self.g_grafo5_krsk.adiciona_aresta('q2', '0', '7', 8)
        self.g_grafo5_krsk.adiciona_aresta('q1', '0', '1', 4)
        self.g_grafo5_krsk.adiciona_aresta('q8', '3', '4', 9)

        self.grafo1 = MeuGrafo()
        self.grafo1.adiciona_vertice("A")
        self.grafo1.adiciona_vertice("B")
        self.grafo1.adiciona_vertice("C")
        self.grafo1.adiciona_vertice("D")
        self.grafo1.adiciona_aresta('a1', 'A', 'B', 1)
        self.grafo1.adiciona_aresta('a2', 'B', 'C', 5)
        self.grafo1.adiciona_aresta('a3', 'A', 'C', 10)
        self.grafo1.adiciona_aresta('a4', 'B', 'D', 7)
        self.grafo1.adiciona_aresta('a5', 'D', 'C', 5)

        self.grafo3 = MeuGrafo()
        self.grafo3.adiciona_vertice("A")
        self.grafo3.adiciona_vertice("B")
        self.grafo3.adiciona_vertice("C")
        self.grafo3.adiciona_vertice("D")
        self.grafo3.adiciona_vertice("E")
        self.grafo3.adiciona_vertice("F")
        self.grafo3.adiciona_aresta("1", "A", "B", 3)
        self.grafo3.adiciona_aresta("2", "F", "B", 10)
        self.grafo3.adiciona_aresta("3", "B", "C", 2)
        self.grafo3.adiciona_aresta("4", "C", "D", 2)
        self.grafo3.adiciona_aresta("5", "D", "E", 3)
        self.grafo3.adiciona_aresta("6", "F", "E", 1)
        self.grafo3.adiciona_aresta("7", "E", "B", 7)

        self.grafo1_pr = MeuGrafo()
        self.grafo1_pr.adiciona_vertice("A")
        self.grafo1_pr.adiciona_vertice("B")
        self.grafo1_pr.adiciona_vertice("C")
        self.grafo1_pr.adiciona_vertice("D")
        self.grafo1_pr.adiciona_aresta('a1', 'A', 'B', 1)
        self.grafo1_pr.adiciona_aresta('a2', 'B', 'C', 5)
        self.grafo1_pr.adiciona_aresta('a5', 'D', 'C', 5)

        self.grafo3_pr = MeuGrafo()
        self.grafo3_pr.adiciona_vertice("A")
        self.grafo3_pr.adiciona_vertice("B")
        self.grafo3_pr.adiciona_vertice("C")
        self.grafo3_pr.adiciona_vertice("D")
        self.grafo3_pr.adiciona_vertice("E")
        self.grafo3_pr.adiciona_vertice("F")
        self.grafo3_pr.adiciona_aresta("6", "F", "E", 1)
        self.grafo3_pr.adiciona_aresta("5", "D", "E", 3)
        self.grafo3_pr.adiciona_aresta("4", "C", "D", 2)
        self.grafo3_pr.adiciona_aresta("3", "B", "C", 2)
        self.grafo3_pr.adiciona_aresta("1", "A", "B", 3)


    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

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

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

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
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))
    def test_dfs(self):
        self.assertEqual(self.g_laco.dfs("K"), (self.g_laco_dfs))
        self.assertEqual(self.g_p.dfs("J"), (self.g_p_dfs))
        self.assertEqual(self.g_p4.dfs("J"), (self.g_p4_dfs))
        self.assertEqual(self.g_teste1.dfs("A"), (self.g_teste1_dfs))
        self.assertEqual(self.g_pe.dfs("P"), (self.g_pe_dfs))
        self.assertEqual(self.g_c.dfs("J"), (self.g_c_dfs))
    def test_bfs(self):
        self.assertEqual(self.g_laco.bfs("K"), (self.g_laco_bfs))
        self.assertEqual(self.g_p.bfs("J"), (self.g_p_bfs))
        self.assertEqual(self.g_p4.bfs("J"), (self.g_p4_bfs))
        self.assertEqual(self.g_teste1.bfs("A"), (self.g_teste1_bfs))
        self.assertEqual(self.g_pe.bfs("P"), (self.g_pe_bfs))
        self.assertEqual(self.g_c.bfs("J"), (self.g_c_bfs))

    def test_prim(self):
        self.assertEqual(self.grafo1.prim(), self.grafo1_pr)
        self.assertEqual(self.grafo3.prim(), self.grafo3_pr)

    def test_kruskall(self):
        self.assertEqual(self.g_grafo1.Kruskall(), self.g_grafo1_krsk)
        self.assertEqual(self.g_grafo2.Kruskall(), self.g_grafo2_krsk)
        self.assertEqual(self.g_grafo3.Kruskall(), self.g_grafo3_krsk)
        self.assertEqual(self.g_grafo5.Kruskall(), self.g_grafo5_krsk)
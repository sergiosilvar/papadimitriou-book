'''
Created on 04/05/2013

@author: Sergio Rodrigues
@contact: srodriguex@gmail.com
'''
import unittest
from algorithms_chapter03 import *

class Test(unittest.TestCase):


    def test_add_edge(self):
        g = Graph(False)
        g.add_edge('A', 'B')
        self.assertTrue(g.has_edge('A','B'))
        self.assertTrue(g.has_edge('B','A'))
        self.assertFalse(g.has_edge('B','C'))
        g.add_edge('C','B')
        self.assertTrue(g.has_edge('B','C'))
        
    def test_add_edge_with_weight(self):
        g = Graph(False)
        g.add_edge('A', 'B',5)
        (v1,v2,w) = g.edge('A','B')
        self.assertEquals(v1,'A')
        self.assertEquals(v2,'B')
        self.assertEquals(w, 5)

        g.add_edge('B', 'A',10)
        (v1,v2,w) = g.edge('A','B')
        self.assertEquals(v1,'A')
        self.assertEquals(v2,'B')
        self.assertEquals(w, 10)

        g.add_edge('B', 'A',-10)
        (v1,v2,w) = g.edge('A','B')
        self.assertEquals(v1,'A')
        self.assertEquals(v2,'B')
        self.assertEquals(w, -10)

        
        self.assertEquals(len(g.edges('B')),1)
        

    def test_remove_edge(self):
        g = Graph(False)
        g.add_edge('A','B')
        g.add_edge('A','C')
        self.assertTrue(g.remove_edge('C','A'))
        self.assertFalse(g.has_edge('A','C'))
        
    def test_vertices(self):
        g = Graph(False)
        g.add_edge('A','B')
        g.add_edge('A','C')
        g.add_edge('C','D')
        g.add_edge('C','B')
        self.assertEquals(set(g.nodes()),set(['A','B','C','D']))
        g.add_edge('F','E')
        self.assertEquals(set(g.nodes()),set(['A','B','C','D','F','E']))
        
        
    def test_edges_from_a_node(self):
        g = Graph(False)
        g.add_edge('A','B')
        l_edges = g.edges('A')
        self.assertEquals(set(l_edges),set([('A','B',1)]))
        g.add_edge('A','C')
        l_edges = g.edges('A')
        self.assertEquals(set(l_edges),set([('A','B',1),('A','C',1)]))
        g.add_edge('B','E')
        l_edges = g.edges('A')
        self.assertEquals(set(l_edges),set([('A','B',1),('A','C',1)]))
        l_edges = g.edges('B')
        self.assertEquals(set(l_edges),set([('B','A',1),('B','E',1)]))
    
    def test_all_edges(self):
        # Not directed edges.
        g = Graph(False)
        g.add_edge('A', 'B')
        g.add_edge('A', 'E')
        g.add_edge('E', 'I')
        g.add_edge('E', 'J')
        g.add_edge('I', 'J')
        g.add_node('F')
        all_edges = g.edges()
        self.assertTrue(('A','B',1) in all_edges)
        self.assertTrue(('B','A',1) in all_edges)
        self.assertTrue(('I','E',1) in all_edges)
        self.assertFalse(('F','A',1) in all_edges)
        self.assertEquals(len(all_edges),10)
        
        # Directed edges.
        h = Graph(True)
        h.add_edge('A', 'B')
        h.add_edge('A', 'E')
        h.add_edge('E', 'I')
        h.add_edge('E', 'J')
        h.add_edge('I', 'J')
        h.add_node('F')
        all_edges = h.edges()
        self.assertTrue(('A','B',1) in all_edges)
        self.assertFalse(('B','A',1) in all_edges)
        self.assertFalse(('I','E',1) in all_edges)
        self.assertTrue(('I','J',1) in all_edges)
        self.assertFalse(('F','A',1) in all_edges)
        self.assertEquals(len(all_edges),5)
        
    def test_add_node(self):
        g = Graph(False)
        self.assertFalse(g.has_node('A'))
        g.add_node('A')
        self.assertTrue(g.has_node('A'))
        g.add_node('B')
        self.assertEquals(set(g.nodes()),set(['A','B']))
        self.assertEquals(len(g.edges('A')),0)
                                          
    def test_dfs(self):
        g = self.create_graph_example()
        
        # Run the dfs on g.
        dfs(g)
          
        # Test if pre and post is equals to the book.
        self.assertEquals(g.pre['A'],1)
        self.assertEquals(g.pre['B'],2)
        self.assertEquals(g.pre['E'],4)
        self.assertEquals(g.pre['I'],5)
        self.assertEquals(g.pre['J'],6)
        self.assertEquals(g.pre['C'],11)
        self.assertEquals(g.pre['D'],12)
        self.assertEquals(g.pre['H'],13)
        self.assertEquals(g.pre['G'],14)
        self.assertEquals(g.pre['L'],18)
        self.assertEquals(g.pre['K'],15)
        self.assertEquals(g.pre['F'],23)
        self.assertEquals(g.post['A'],10)
        self.assertEquals(g.post['B'],3)
        self.assertEquals(g.post['E'],9)
        self.assertEquals(g.post['I'],8)
        self.assertEquals(g.post['J'],7)
        self.assertEquals(g.post['C'],22)
        self.assertEquals(g.post['D'],21)
        self.assertEquals(g.post['H'],20)
        self.assertEquals(g.post['G'],17)
        self.assertEquals(g.post['L'],19)
        self.assertEquals(g.post['K'],16)
        self.assertEquals(g.post['F'],24)
        
        # Test the connected components.
        cc = g.connected_components()
        cc_expected = [['A', 'B', 'E', 'I', 'J'],['C', 'D', 'G', 'H', 'K', 'L'],['F']]
        self.assertEquals(cc[0],cc_expected[0])
        self.assertEquals(cc[1],cc_expected[1])
        self.assertEquals(cc[2],cc_expected[2])

    def test_iterative_dfs(self):
        g = self.create_graph_example()
        
        # Run the dfs on g.
        iterative_dfs(g)
          
        # Test if pre and post is equals to the book.
        self.assertEquals(g.pre['A'],1)
        self.assertEquals(g.pre['B'],2)
        self.assertEquals(g.pre['E'],4)
        self.assertEquals(g.pre['I'],5)
        self.assertEquals(g.pre['J'],6)
        self.assertEquals(g.pre['C'],11)
        self.assertEquals(g.pre['D'],12)
        self.assertEquals(g.pre['H'],13)
        self.assertEquals(g.pre['G'],14)
        self.assertEquals(g.pre['L'],18)
        self.assertEquals(g.pre['K'],15)
        self.assertEquals(g.pre['F'],23)
        self.assertEquals(g.post['A'],10)
        self.assertEquals(g.post['B'],3)
        self.assertEquals(g.post['E'],9)
        self.assertEquals(g.post['I'],8)
        self.assertEquals(g.post['J'],7)
        self.assertEquals(g.post['C'],22)
        self.assertEquals(g.post['D'],21)
        self.assertEquals(g.post['H'],20)
        self.assertEquals(g.post['G'],17)
        self.assertEquals(g.post['L'],19)
        self.assertEquals(g.post['K'],16)
        self.assertEquals(g.post['F'],24)
        
        # Test the connected components.
        cc = g.connected_components()
        cc_expected = [['A', 'B', 'E', 'I', 'J'],['C', 'D', 'G', 'H', 'K', 'L'],['F']]
        self.assertEquals(cc[0],cc_expected[0])
        self.assertEquals(cc[1],cc_expected[1])
        self.assertEquals(cc[2],cc_expected[2])

    def test_nodes_from(self):
        g = self.create_graph_example()
        self.assertEquals(set(g.nodes_from('A')), set(['B','E']))
        self.assertEquals(set(g.nodes_from('F')), set([]))
        
    
    
    def create_graph_example(self):
        # The graph from Figure 3.6, page 97.
        g = Graph(False)
        g.add_edge('A', 'B')
        g.add_edge('A', 'E')
        g.add_edge('E', 'I')
        g.add_edge('E', 'J')
        g.add_edge('I', 'J')
        g.add_node('F')
        g.add_edge('C', 'D')
        g.add_edge('C', 'G')
        g.add_edge('C', 'H')
        g.add_edge('D', 'H')
        g.add_edge('G', 'H')
        g.add_edge('G', 'K')
        g.add_edge('H', 'K')
        g.add_edge('H', 'L')
        return g

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
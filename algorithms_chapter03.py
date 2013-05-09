'''
Created on 02/05/2013

@author: Sergio Rodrigues
@contact: srodriguex@gmail.com
'''


class Graph:


    _directed = None
    _dict_weight = None
    _list_adj = None
    _cc = 0
    _clock = 0
    
    # Structures from the book.
    visited = {} # Identifies whether a node was visited.
    ccnum = {} # Identifies the connected component of a node.
    pre = {} # Identifies the start visit order.
    post = {} # Identifies the end visit order.
    
    def __init__(self,directed=False):
        self._directed = directed
        self._dict_weight = {}
        self._list_adj = {}
        self._cc = 0
        self._clock = 0

    def add_edge(self, v1,v2,w=1):
        '''
        Adds and edge (v1,v2,w) with optional weight "w".
        If it already exists, updates the weight.
        If the Graph is not directed, adds edge (v2,v1,w).
        @param v1: Start node of the edge.
        @param v2: End node of the edge.
        @param w: Weight of the edge. Default is "1".
        '''
        
        def _add_edge(v1,v2,w):
            '''
            Adds the directed edge (v1,v2,w) in the graph.
            @param v1: Start node of the edge.
            @param v2: End node of the edge.
            @param w: Wieht of the edge.
            '''
            if not self._list_adj.has_key(v1):
                self._list_adj[v1]= []
            l_nodes_from_v1 = self._list_adj[v1]
            if l_nodes_from_v1.count(v2) == 0:
                l_nodes_from_v1.append(v2)
            self._dict_weight[(v1,v2)] = w

        # Adds the directed edge.
        _add_edge(v1,v2,w)
        
        # If the Graph is not directed, create the other edge.
        if not self._directed:
            _add_edge(v2,v1,w)
            
    def has_edge(self,v1,v2):
        _result = False
        if self._list_adj.has_key(v1):
            l = self._list_adj[v1]
            _result =  l.count(v2) > 0
        return _result
    
    def has_node(self,v):
        return self._list_adj.has_key(v)
    
    def remove_edge(self,v1,v2):
        _result = False
        l = self._list_adj[v1]
        l.remove(v2)
        if not self._directed:
            l = self._list_adj[v2]
            l.remove(v1)
        _result = True
        return _result
        
    def add_node(self,v):
        if not self.has_node(v):
            self._list_adj[v]= []
        
    def nodes(self):
        '''
        @return List of nodes.
        '''
        l = self._list_adj.keys()
        l.sort()
        return l
    
    def nodes_from(self,v):
        '''
        @return A list of nodes reachable from "v".
        @param v: A given node.
        '''
        _result = []
        l_edges = self.edges(v)
        for (x,y,w) in l_edges:
            _result.append(y)
        return _result
    
    
    def edges(self,v=None):
        '''
        @return A list of edges as tuples (v,i,w) for all nodes "i" reachable from "v", with weight "w".
        @param v: An optional node. If omitted, all edges are returned.
        '''
        _result = []
        if v != None:
            l_nodes_reachable_from_v = self._list_adj[v]
            for i in l_nodes_reachable_from_v:
                _result.append(self.edge(v, i))
        else:
            # For each node and its adjecency 
            for (v,l_adj) in self._list_adj.iteritems():
                for u in l_adj:
                    _result.append(self.edge(v, u))
        return _result
    
    def edge(self,v1,v2):
        '''
        @return Edge as tuple (v1,v2,w), where "w" is the weight of the edge (v1,v2).
        @param v1: Stard node.
        @param v2: End node.
        '''
        w = self._dict_weight[(v1,v2)]
        return (v1,v2,w)
    
    def connected_components(self):
        '''
        @return A list of connected components. Each connected component is list of nodes.
        '''
        cc = {}
        for (key,value) in self.ccnum.iteritems():
            if not cc.has_key(value):
                cc[value] = []
            cc[value].append(key)
        return cc
    
            
# FIXME:Remove
# Book structures for "explore".
#_cc = 0 # The connected component id.
#_clock = 0 # Identifies the "prevsit" and "postvisit" order of the nodes during "explore".
    
def previsit(G,v):
    # FIXME: Remove
    #global _clock # Python requirement to write on global variables.
    G.ccnum[v] = G._cc
    G.pre[v] = G._clock
    G._clock += 1
 
def postvisit(G,v):
    # FIXME: Remove
    #global _clock
    G.post[v] = G._clock
    G._clock += 1
    
def explore(G, v):
    '''
    Find all nodes reachable from a particular node.
    p. 95.
    @param G: A Graph.
    @param v: The initial node.
    @return: Dictionary visited(u) set to true for all nodes "u" reachable from "v".
    '''  
    G.visited[v] = True
    previsit(G,v)
    for (v,u,w) in G.edges(v):
        if not G.visited[u]:
            explore(G,u)
    postvisit(G,v)
    
def iterative_explore(G, v):
    def first_node_not_visited_from(self,v):
        '''
        A helper function for iterative_explore.
        @return The first node not visited from "v".
        @param v: A given node.
        '''
        l_edges = self.edges(v)
        for (x,y,w) in l_edges:
            if not self.visited[y]: 
                return y
        return None
       
    q = []
    previsit(G,v)
    G.visited[v] = True
    q.append(v)
    while len(q)>0:
        top = q[len(q)-1]
        u = first_node_not_visited_from(G,top)
        if u!=None:
            previsit(G,u)
            G.visited[u] = True
            q.append(u)
        else:
            postvisit(G, top)
            q.pop()
    
def dfs(G):
    '''
    Deep-first search on graph G.
    @param G: A Graph.
    '''
    
    # FIXME Remove
    # Python requirement to write on global variables.
    #global _cc 
    #global _clock
    
    _setup_dfs(G)    
    for v in G.nodes():
        if not G.visited[v]:
            explore(G,v)
            G._cc += 1 # Increments the component connected id as a new node will be visited from a new explore.
           
def iterative_dfs(G):
    '''
    Uses the iterative deep-first version on graph G.
    @param G: A Graph.
    '''
    
    # FIXME Remove
    # Python requirement to write on global variables.
    #global _cc 
    #global _clock
    
    _setup_dfs(G)    
    for v in G.nodes():
        if not G.visited[v]:
            iterative_explore(G,v)
            G._cc += 1 # Increments the component connected id as a new node will be visited from a new explore.

def _setup_dfs(G):
    G._cc = 0 # The component connected id.
    G._clock = 1 # The visit order starts at 1, as seen on page 97, figure 3.6, item (b).
    for v in G.nodes():
        G.visited[v] = False
        G.ccnum[v] = -1
        G.pre[v] = -1
        G.post[v] = -1
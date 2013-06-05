'''
Created on 27/05/2013

@author: sergio
'''

from algorithms_chapter03 import Graph
import networkx as nx
import matplotlib.pylab as plt

def longest_increasing_subsequence2(li):
    '''
    Compute the longest increasing subsequence.
    p. 170.
    Use 3rd graph library 'Networkx' for the sake of the programmer.
    @param li - List of integers.
    '''
    
    
    # Create and populate the edges as restricted by comparison.
    G = nx.DiGraph()
    for start in range(len(li)-1):
        for end in range(start,len(li)):
            if li[start] < li[end]:
                node_start = (start, li[start])
                node_end = (end,li[end])
                G.add_edge(node_start, node_end)
    
    # Execute the algorithm.
    G_r = G.reverse(copy=True) # To copmute (i,j) in E for any j.
    
    L = [-1 for i in range(len(li))] # Length of the longest path.
    prev = [-1 for i in range(len(li))] # .
    for j in range (len(li)):
        # Computing L(j) = 1 + max{L(i):(i,j) in E}
        max_L_i = 0
        max_i = -1
        for i,v in G_r[(j,li[j])]:
            if  L[i] > max_L_i:
                max_L_i = L[i] 
                max_i = i
        L[j] = 1 + max_L_i
        prev[j] = max_i

    # Show results. Note index i starts at 0.
    print 'Max path is:'+ str(max(L))
    i = L.index(max(L))
    path = 'DNE'
    while i >=0:
        path += ' >- ' + str(li[i])
        i = prev[i]
    print 'Path: ' + path[::-1]
#    nx.draw_circular(G)
#    plt.show()
#    plt.savefig("longest_increasing_subsequence2.png")    

if __name__ == '__main__':
    longest_increasing_subsequence2([5,2,8,6,3,6,9,7])

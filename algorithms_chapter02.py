'''
    Algorithms from S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani
    Chapter 02
    
    @author: Sergio Rodrigues
    @contact: srodriguex@gmail.com
'''
import random
def _to_bin(i):
    '''
    @return: Binary string representation of 'i'. Eg: '1101'=13
    @param i: Integer to be converted.
    '''
    return bin(i)[2:]

def _to_int(s):
    '''
    @return: Integer number.
    @param s: Binary string representation. 
    '''
    return int(s,2)

def _leftmost(n,k):
    return n>>k

#FIXME: Improve below.
def _rightmost(n,k):
    return _to_int(_to_bin(n)[-k:])
    
    

def multiply(x,y):
    '''
    A divide and conquer algorithm for integer multiplication.
    @return: Their product.
    @param x: integer.
    @param y: integer.
    '''

    #FIXME:Inneficient way in discovering max without using log or multiplications.
    n = max(len(_to_bin(x)),len(_to_bin(y)))
    
    if n==1:return x&y
    
   
    x_l,x_r = _leftmost(x, (n)/2), _rightmost(x, n/2)
    y_l,y_r = _leftmost(y, (n)/2), _rightmost(y, n/2)
    
    # Uncomment the line below to debug.
    #print 'x:%s, y:%s, x_l:%s, x_r:%s, y_l:%s, y_r:%s' % (_to_bin(x), _to_bin(y), _to_bin(x_l),_to_bin(x_r),_to_bin(y_l),_to_bin(y_r))
    
    p_1 = multiply(x_l,y_l)
    p_2 = multiply(x_r,y_r)
    p_3 = multiply(x_l+x_r,y_l+y_r)
    return (p_1<<n)+((p_3-p_1-p_2)<<((n)/2))+p_2

def merge(x, y):
    '''
    Merge ascending two lists of intgers into one.
    p. 61
    @param x: One list of integers.
    @param y: Another list of integers.
    '''
    if len(x)==0:
        return y
    if len(y)==0:
        return x
    if x[0] <= y[0]:
        return [x[0]]+merge(x[1:],y)
    else:
        return [y[0]]+merge(x,y[1:])


def mergesort(a):
    '''
    Sort the given list.
    p. 60.
    @return: A sorted array of the input.
    @param a: An array of integers, unsorted.
    '''
    n = len(a)
    if n > 1:
        return merge(mergesort(a[:n/2]),mergesort(a[n/2:]))
    else:
        return a

def iterative_mergesort(a):
    '''
    Does the same as mergesort above, but without recursion.
    p. 62.
    @param a: A list of elements to be sorted.
    '''
    def inject(e):
        q.append(e)
    def eject():
        if len(q)>0:
            return q.pop(0)    
        return None
    
    q = []
    n = len(a)
    for i in range(n):
        inject([a[i]]) # Python specific.
    while len(q)>1:
        m = merge(eject(),eject())
        inject(m)
    return eject()

def selection(S,k):
    '''
    @return:  The k-th smallest element from of "S".
    p. 64.
    @param S: An unordered list of numbers.
    @param k: The order of the smallest element to be found inside the list "S". 
    '''
   
    v = S[random.randint(0,len(S)-1)]
    
    
    # TODO: List comprehension isn't working. Why?
    # Sl: A list of elements from "S" smaller than "v".
#    Sl = [S[i] for i in range(len(S)) if S[i] < v]
    # Sv: A list of elements from "S" equals to "v".
#    Sv = [S[i] for i in range(len(S)) if S[i] == v]
    # Sr: A list of elements from "S" greater than "v".
#    Sr = [S[i] for i in range(len(S)) if S[i] > v]

    # FIXME: For now I'm using classic for while list comprehension sucks.
    Sl,Sv,Sr = [],[],[]
    n = len(S)
    for i in range(n):
        if S[i] < v:
            Sl.append(S[i])
        if S[i] == v:
            Sv.append(S[i])
        if S[i] > v:
            Sr.append(S[i])
    
    if k <= len(Sl):
        return selection(Sl, k)
    elif len(Sl) < k and k <= (len(Sl)+len(Sv)):
        return v
    elif k > len(Sl) + len(Sv):
        return selection(Sr,k-len(Sl)-len(Sv)) 
    

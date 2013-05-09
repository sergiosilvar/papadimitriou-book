'''
    Algorithms from S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani
    Chapter 01
    
    @author: Sergio Rodrigues
    @contact: srodriguex@gmail.com
'''

from random import randint

def multiply(x,y):
    '''
    Multiplication a la Francais.
    Figure 1.1, p. 25.
    @return: Product x*y integer.
    @param x: The mutiplicand, must be integer and positive.
    @param y: The multiplicator, must be integer and positive.
    '''
    
    if y == 0:
        return 0
    z = multiply(x,y>>1) #Bitwise division by 2 on y.
    if not y&1:
        return (z<<1) #Bitwise multiplicaiton by 2 on z.
    else:
        return x + (z<<1)

def division(x,y):
    '''
    Division.
    Figure 1.2, p. 26.
    @return: Tuple (q,r) with the quotient 'q' and remainder 'r' of x divided by y>0.
    @param x: The dividend, must be integer and positive.
    @param y: The divisor, must be integer and positive.
    '''
    if x==0: 
        return (0,0)
    (q,r) = division(x>>1, y)
    q = q<<1
    r = r<<1
    if x&1: #odd
        r += 1
    if r>=y:
        r -= y
        q += 1
    return (q,r)

def modeexp(x,y,n):
    '''
    Modular exponentitiaton x**y (mod n).
    Figure 1.4, p. 29.
    @return: The rest of division (x**y)/n.
    @param x: The base, integer.
    @param y: The exponent, integer and positive.
    @param n: The modulus, integer and positive.
    '''
    
    if y == 0:
        return 1
    z = modeexp(x,y/2,n)
    if y % 2 == 0:
        return (z**2) % n
    else:
        return ( x*z**2 ) % n

def euclid(a,b):
    '''
    Euuclid's Greatest Commom Divisor (gcd) algorithm.
    Figure 1.5, p. 30
    @return: The gdc(a,b).
    @param a: integer positive.
    @param b: integer positive.
    '''
    if b==0:
        return a
    return euclid(b, a % b)

def extended_euclid(a, b):
    '''
    Extended Euuclid's Greatest Commom Divisor algorithm.
    Figure 1.6, p. 31.
    @return:  Tuple (x, y, d) as d = gcd(a, b)= a*x + b*y.
    @param a: integer, positive.
    @param b: integer, positive.
    '''
    if b == 0:
        return (1, 0, a)
    (x0, y0, d) = extended_euclid(b, a % b)
    return (y0, (x0 -(a/b)*y0), d)

def primality(n):
    '''
    An algorithm for testing primality.
    Figure 1.7, p. 35.
    @return: True whether n is prime.
    @warning: Can't assert Carmichael numbers correctly.
    @param n: Integer to be tested if is prime.
    '''
    
    a = randint(2,n-1)
    if modeexp(a, n-1, n) == 1:
        return True
    else:
        return False
    
def primality2(n,k=None):
    '''
    An algorithm for testing primality, with low error probability.
    Figure 1.7, p. 35.
    @return: True whether n is prime.
    @warning: Low error probability, about < 1/2**k.
    @param n: Integer to be tested if is prime.
    @param k: Optional. Number of tests to be done for 'n'. If omitted, it's set to 100.
    '''
    if k==None:
        k = 100
    list_a = [randint(2,n-1) for i in range(1,k+1)]
    for a in list_a:
          if modeexp(a, n-1, n) != 1:
            return False
    return True

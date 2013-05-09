'''
Created on 06/04/2013
Test module for "algorithms_chapter01.py".
@author: Sergio Rodrigues
@contact: srodriguex@gmail.com

'''

from algorithms_chapter01 import multiply
from algorithms_chapter01 import division
from algorithms_chapter01 import modeexp
from algorithms_chapter01 import euclid
from algorithms_chapter01 import extended_euclid
from algorithms_chapter01 import primality
from algorithms_chapter01 import primality2
import unittest


class Test(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(3,2),6)
        self.assertEqual(multiply(2,3),6)
        self.assertEqual(multiply(3,5),15)
        self.assertEqual(multiply(3456,9876),34131456)
        
    def test_division(self):
        self.assertEqual(division(4,2),(2,0))
        self.assertEqual(division(5,2),(2,1))
        self.assertEqual(division(7464637,3648),(2046,829))
        
    def test_modeexp(self):
        self.assertEqual(modeexp(5, 20,7),4)
        self.assertEqual(modeexp(7, 1001,11),7)
        self.assertEqual(modeexp(2, 130, 263),132)
        self.assertEqual(modeexp(2, 5432675,13),7)

    def test_euclid(self):
        self.assertEqual(euclid(1234, 54), 2)
        self.assertEqual(euclid(6643, 2873), 13)
        self.assertEqual(euclid(1035, 759),69)

    def test_extended_euclid(self):
        self.assertEqual(extended_euclid(13, 4), (1,-3,1))
        self.assertEqual(extended_euclid(6643, 2873), (-16,37,13))
        self.assertEqual(extended_euclid(272828282, 3242), (697,-58655556,2))
        
    def test_primality(self):
        # Not a prime.
        self.assertFalse(primality(12345678))
        
        # Some primes.
        self.assertTrue(primality(17))
        self.assertTrue(primality(15487399))
        
        # Biggest prime in http://www.bigprimes.net.
        self.assertTrue(primality(32416190071))
    
        # The Carmichael Number on page 38 fools the algorithm.
        self.assertTrue(primality(561))
        
        # Funny, this is a Carmichael Number, and the algorithm nails it!
        self.assertFalse(primality(60351))
        
        # But this is another pseudoprime, and we miss it. 
        # Check it for more at http://mathworld.wolfram.com/CarmichaelNumber.html.
        self.assertTrue(primality(2467))
        
    def test_primality2(self):
        
        # Number of tests on the number.
        k = 100
        
        # Some primes just to warm up.
        self.assertTrue(primality2(17,k))
        self.assertTrue(primality2(15487399,k))
 
        # Not a prime. No problem to check it.
        self.assertFalse(primality2(12345678,k))

        # First challenge. The Carmichael Number on page 38 still rarely fools the algorithm.
        self.assertFalse(primality2(561),"Fail, 561 is a Charmichael Number!")
                
        # Other pseudoprimes. http://en.wikipedia.org/wiki/Fermat_pseudoprime
        for p in [1729,8911,10585,15841,29341,41041,46657,52633]:
            self.assertFalse(primality2(p), str(p)+" is a pseudoprime! We were to assert False.")
            
        # Biggest prime in http://www.bigprimes.net. Well done.
        self.assertTrue(primality2(32416190071,k))
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
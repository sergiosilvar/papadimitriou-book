'''
Created on 07/04/2013
Test module for "algorithms_chapter02.py".
@author: Sergio Rodrigues
@contact: srodriguex@gmail.com

'''
from algorithms_chapter02 import _to_bin,_to_int,_leftmost,_rightmost,multiply,merge,mergesort,iterative_mergesort,selection
import unittest

class Test(unittest.TestCase):



    def test_to_bin(self):
        self.assertEquals(_to_bin(0),'0') 
        self.assertEquals(_to_bin(1),'1') 
        self.assertEquals(_to_bin(5),'101') 
        self.assertEquals(_to_bin(2),'10') 
        self.assertEquals(_to_bin(15),'1111') 
        self.assertEquals(_to_bin(65555),'10000000000010011') 
        
    def test_leftmost(self):
        self.assertEquals(_leftmost(_to_int('1'),1), _to_int('0'))
        self.assertEquals(_leftmost(_to_int('10'),1), _to_int('1'))
        self.assertEquals(_leftmost(_to_int('01'),1), _to_int('0'))
        self.assertEquals(_leftmost(_to_int('01'),3), _to_int('0'))
        self.assertEquals(_leftmost(_to_int('1011'),1), _to_int('101'))
        self.assertEquals(_leftmost(_to_int('10011001'),3), _to_int('10011'))
        self.assertEquals(_leftmost(_to_int('10000000000010011'),4),65555/2**4) 
     
    def test_rightmost(self):
        self.assertEquals(_rightmost(_to_int('1'),0), _to_int('1'))
        self.assertEquals(_rightmost(_to_int('1'),1), _to_int('1'))
        self.assertEquals(_rightmost(_to_int('01'),1), _to_int('1'))
        self.assertEquals(_rightmost(_to_int('101'),2), _to_int('1'))
        self.assertEquals(_rightmost(_to_int('1011'),3), _to_int('11'))
        self.assertEquals(_rightmost(_to_int('10011001'),4), _to_int('1001'))
        self.assertEquals(_rightmost(_to_int('10000000000010011'),5),_to_int('00010011') )
    
    def test_multiply(self):
        self.assertEquals(multiply(1, 1),1)
        self.assertEquals(multiply(1, 0),0)
        self.assertEquals(multiply(1, 2),2)
        self.assertEquals(multiply(2, 1),2)
        self.assertEquals(multiply(2, 3),6)
        self.assertEquals(multiply(8, 8),64)


 
        
    def test_merge(self):
        self.assertEquals(merge([2],[1]),[1,2])
        self.assertEquals(merge([2,3],[1]),[1,2,3])
        self.assertEquals(merge([1,3,9],[0,6,7]),[0,1,3,6,7,9])
       
    def test_mergesort(self):
        self.assertEquals(mergesort([5,3]), [3,5])
        self.assertEquals(mergesort([5,3,-1]), [-1,3,5])
        self.assertEquals(mergesort([5,1,6,3,-1]), [-1,1,3,5,6])
        self.assertEquals(mergesort([10,8,1,4,7,3,9,5,2,6]),[1,2,3,4,5,6,7,8,9,10])
    
    def test_iterative_mergesort(self):
        self.assertEquals(iterative_mergesort([5,3]), [3,5])
        self.assertEquals(iterative_mergesort([5,3,-1]), [-1,3,5])
        self.assertEquals(iterative_mergesort([10,8,1,4,7,3,9,5,2,6]),[1,2,3,4,5,6,7,8,9,10])
      
    def test_selection(self):
        self.assertEquals(selection([1],1),1)
        self.assertEquals(selection([1,2],1),1)
        self.assertEquals(selection([1,2,3],2),2)
        self.assertEquals(selection([3,6,9],2),6)
        self.assertEquals(selection([10,8,1,4,7,3,9,5,2,6],8),8)
        
        # Using this list unordered: [-100, -20, 20, 30, 40, 40, 50, 70, 90, 100].
        self.assertEquals(selection([100,50,30,-20,-100,40,40,90,20,70],5),40)
        self.assertEquals(selection([100,50,30,-20,-100,40,40,90,20,70],6),40)
        self.assertEquals(selection([100,50,30,-20,-100,40,40,90,20,70],7),50)
        

        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
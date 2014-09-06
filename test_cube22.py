'''
Created on 2014/08/27

@author: alchu
'''
import unittest
from cube22 import Cube22

class Test(unittest.TestCase):


    def testInit(self):
        Cube22()
        
    def test_equal(self):
        c1 = Cube22()
        c2 = Cube22()
        self.assertEqual(c1, c2)
        c2._data[7] = "XZy"
        self.assertNotEqual(c1, c2)

    def test_right(self):
        c = Cube22()
        c.right(1)
        self.assertEqual(c._data, ["XYZ", "XZy", "XYZ", "XZy", "XYZ", "XZy", "XYZ", "XZy"])
        c.right(3)
        self.assertEqual(c, Cube22())

    def test_back(self):
        c = Cube22()
        c.back(1)
        self.assertEqual(c._data, ["XYZ", "XYZ", "zYX", "zYX", "XYZ", "XYZ", "zYX", "zYX"])
        
    def test_top(self):
        c = Cube22()
        c.top()
        self.assertEqual(c._data, ["XYZ", "XYZ", "XYZ", "XYZ", "YxZ","YxZ","YxZ","YxZ"])

    def test_tostr(self):
        c = Cube22()
        self.assertEqual(c.tostr(), "XYZ"*8)
        c.top()
        self.assertEqual(c.tostr(), "XYZ"*4+"YxZ"*4)
        
    def test_horisearch(self):
        c = Cube22()
        route = c.horisearch(["XYZ"]*4+["Xyz"]*4)
        self.assertEqual(route, ["T2"])
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInit']
    unittest.main()
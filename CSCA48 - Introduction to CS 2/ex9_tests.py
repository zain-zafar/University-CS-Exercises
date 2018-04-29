from ex9 import *
import unittest

class Test_Inits(unittest.TestCase):

    def test_init_(self):
        a = Heap([1,2,3])
        result = [3,2,1]
        self.assertEqual(result, [1,2,3])

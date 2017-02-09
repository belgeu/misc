import unittest
 
class UnitTest(unittest.TestCase):
 
    def setUp(self):
        print "Starting..."
 
    def test_1(self):
        self.assertEqual( True, True)
 
    def test_2(self):
        self.assertEqual( False, False)
 
if __name__ == '__main__':
    unittest.main()
import unittest, Boggle

class BoggleTest(unittest.TestCase):
    
    def test_neighbours(self):
        for i in range(len(Boggle.dice)):
            self.assertFalse(i in Boggle.neighbours[i], "included self in neighbours")
            self.assertFalse(-1 in Boggle.neighbours[i], "included -1 in neighbours")
            self.assertFalse(16 in Boggle.neighbours[i], "included 16 in neighbours")
        
        self.assertTrue(1 in Boggle.neighbours[0], "did not include 1 in neighbours of 0")
        self.assertTrue(5 in Boggle.neighbours[0], "did not include 5 in neighbours of 0")


if __name__ == '__main__':
    unittest.main()
    
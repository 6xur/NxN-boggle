import unittest, Boggle

TEST_BOARD = ['R', 'H', 'R', 'E',
             'Y', 'P', 'C', 'S', 
             'W', 'N', 'S', 'N',
             'T', 'E', 'G', 'O']

class BoggleTest(unittest.TestCase):
    
    
    def test_neighbours(self):
        for i in range(len(Boggle.dice)):
            self.assertNotIn(i, Boggle.all_neighbours[i], "included self in neighbours")
            self.assertNotIn(-1, Boggle.all_neighbours[i], "included -1 in neighbours")
            self.assertNotIn(16, Boggle.all_neighbours[i], "included 16 in neighbours")
        
        self.assertIn(1, Boggle.all_neighbours[0], "did not include 1 in neighbours of 0")
        self.assertIn(4, Boggle.all_neighbours[0], "did not include 4 in neighbours of 0")
        self.assertIn(5, Boggle.all_neighbours[0], "did not include 5 in neighbours of 0")


    def test_boggle(self):
        sln = Boggle.solve_boggle(TEST_BOARD)
        print("found " + str(len(sln)))
        self.assertTrue("EGO" in sln, "Did not contain EGO")
        self.assertTrue("SENT" in sln, "Did not contain SENT")
        self.assertTrue("WENT" in sln, "Did not contain WENT")
        self.assertTrue("PRESS" in sln, "Did not contain PRESS")
        self.assertTrue("CRESS" in sln, "Did not contain CRESS")
        self.assertTrue("ONSET" in sln, "Did not contain ONSET")
        self.assertTrue("SONG" in sln, "Did not contain SONG")
        self.assertFalse("WEST" in sln, "Contained WEST but should not")
        self.assertFalse("GO" in sln, "Contained GO but should not")
        self.assertFalse("SONGS" in sln, "Contained SONGS but should not")
        self.assertFalse("RHETORIC" in sln, "Contained RHETORIC but should not")
        
        
if __name__ == '__main__':
    unittest.main()
    
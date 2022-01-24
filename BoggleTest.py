import unittest, boggle_old

TEST_BOARD = ["L", "B", "L",
              "O", "O", "F",
              "T", "U", "D"]

class BoggleTest(unittest.TestCase):
    
    
    def test_boggle(self):
        sln = boggle_old.solve_boggle(TEST_BOARD)
        print("found " + str(len(sln)))
        self.assertTrue("TOD" in sln, "Did not contain EGO")
        self.assertFalse("GO" in sln, "Contained GO but should not")
        self.assertFalse("SONGS" in sln, "Contained SONGS but should not")
        self.assertFalse("RHETORIC" in sln, "Contained RHETORIC but should not")  
        
        
if __name__ == '__main__':
    unittest.main()
    
import unittest, boggle

TEST_BOARD = ["L", "B", "L",
              "O", "O", "F",
              "T", "U", "D"]

class BoggleTest(unittest.TestCase):
    
    def test_neighbours(self):
        boggle.set_all_neighbours(TEST_BOARD)
        for i in range(len(TEST_BOARD)):
            self.assertNotIn(i, boggle.all_neighbours[i])
            self.assertNotIn(-1, boggle.all_neighbours[i])
            self.assertNotIn(16, boggle.all_neighbours[i])
        
        self.assertSetEqual(boggle.all_neighbours[0], {1, 3, 4})
        self.assertSetEqual(boggle.all_neighbours[1], {0, 2, 3, 4, 5})
        self.assertSetEqual(boggle.all_neighbours[2], {1, 4, 5})
        self.assertSetEqual(boggle.all_neighbours[3], {0, 1, 4, 6, 7})
        self.assertSetEqual(boggle.all_neighbours[4], {0, 1, 2, 3, 5, 6, 7, 8})
        self.assertSetEqual(boggle.all_neighbours[5], {1, 2, 4, 7, 8})
        self.assertSetEqual(boggle.all_neighbours[6], {3, 4, 7})
        self.assertSetEqual(boggle.all_neighbours[7], {3, 4, 5, 6, 8})
        self.assertSetEqual(boggle.all_neighbours[8], {4, 5, 7})

    def test_boggle(self):
        sln = boggle.solve_boggle(TEST_BOARD)
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
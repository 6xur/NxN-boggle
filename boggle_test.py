import unittest, boggle

TEST_BOARD = ["L", "B", "L",
              "O", "O", "F",
              "T", "U", "D"]

boggle.set_all_neighbours(TEST_BOARD)

class BoggleTest(unittest.TestCase):
    # test suite for boggle solver
    
    def test_all_neighbours(self):
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


    def test_solve_boggle(self):
        solutions = boggle.solve_boggle(TEST_BOARD)
        self.assertTrue("DUO" in solutions, "Did not contain DUO")
        self.assertTrue("TOD" in solutions, "Did not contain TOD")
        self.assertTrue("OUT" in solutions, "Did not contain OUT")
        self.assertTrue("BOOT" in solutions, "Did not contain BOOT")
        self.assertTrue("LOOT" in solutions, "Did not contain LOOT")
        self.assertTrue("TOOL" in solutions, "Did not contain TOOL")
        self.assertFalse("BOLD" in solutions, "Contained BOLD but should not")
        self.assertFalse("DOLL" in solutions, "Contained DOLL but should not")  
        self.assertFalse("TOLD" in solutions, "Contained TOLD but should not")
        

if __name__ == '__main__':
    unittest.main()
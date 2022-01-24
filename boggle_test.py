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
        self.assertIn("DUO", solutions)
        self.assertIn("TOD", solutions)
        self.assertIn("OUT", solutions)
        self.assertIn("BOOT", solutions)
        self.assertIn("LOOT", solutions)
        self.assertIn("LOOT", solutions)
        self.assertNotIn("BOLD", solutions)
        self.assertNotIn("DOLL", solutions)
        self.assertNotIn("FOOD", solutions)
        self.assertNotIn("TOLD", solutions)


    def test_bogglable(self):
        self.assertTrue(boggle.bogglable("LOB", TEST_BOARD))
        self.assertTrue(boggle.bogglable("BOT", TEST_BOARD))
        self.assertTrue(boggle.bogglable("BUT", TEST_BOARD))
        self.assertFalse(boggle.bogglable("TO", TEST_BOARD))
        self.assertFalse(boggle.bogglable("FOR", TEST_BOARD))
        self.assertFalse(boggle.bogglable("TOT", TEST_BOARD))
        self.assertFalse(boggle.bogglable("FRIENDSHIP", TEST_BOARD))
        
        
if __name__ == '__main__':
    unittest.main()
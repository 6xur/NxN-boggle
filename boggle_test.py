import unittest
import boggle
from string import ascii_uppercase

TEST_BOARD = ["L", "B", "L",
              "O", "O", "F",
              "T", "U", "D"]

boggle.set_all_neighbours(TEST_BOARD)


class BoggleTest(unittest.TestCase):
    # Test suite for boggle
    
    def test_make_board(self):
        # Ensure that the board size is equal to (row_length * row_length)
        board = boggle.make_board(3)
        self.assertEqual(len(board), 9)
        # Ensure that each position contains a uppercase letter
        for letter in board:
            self.assertIn(letter, ascii_uppercase)
    
    
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
    
    
    def test_read_words(self):
        dictionary = set()
        prefixes = set()
        boggle.read_words("dictionary.txt", dictionary, prefixes)
        self.assertGreater(len(dictionary), 0)
        self.assertGreater(len(prefixes), 0)

        
if __name__ == '__main__':
    unittest.main()
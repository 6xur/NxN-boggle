import unittest
import boggle
from string import ascii_uppercase

TEST_BOARD = ["L", "B", "L",
              "O", "O", "F",
              "T", "U", "D"]

boggle.set_all_neighbours(TEST_BOARD)


class BoggleTest(unittest.TestCase):
    # Test suite for boggle
    
    def test_read_words(self):
        dictionary, prefixes = boggle.read_words("dictionary.txt")
        self.assertGreater(len(dictionary), 0)
        self.assertGreater(len(prefixes), 0)
    
    
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

        
    def test_boggle_contain(self):
        solutions = boggle.solve_boggle(TEST_BOARD)
        possible_words = {"DUO", "TOD", "OUT", "LOO", "LOT", "OUD", "LOB",
                          "BOOT", "LOOT", "FOOT", "TOFU", "FOOL", "BLOT"}
        for word in possible_words:
            self.assertIn(word, solutions)
    
    
    def test_boggle_not_contain(self):
        solutions = boggle.solve_boggle(TEST_BOARD)
        impossible_words = {"BOLD", "DOLL", "FOOD", "TOLD", "BOLT", "TOOT"}
        for word in impossible_words:
            self.assertNotIn(word, solutions)

        
if __name__ == '__main__':
    unittest.main()
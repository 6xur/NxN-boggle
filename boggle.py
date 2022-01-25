import math
import random
import time
from typing import List, Set

dice = ["AJBBOO","AFFPSK","ANEAGE","APSHCO", 
        "QNUMHI","ZNHRLN","TDSTYI","TTWOOA",
        "TLRYET","TUMIOC","EDVLRY","EDRLXI",
        "EEGNHW","EIOTSS","ERHTWV","EENUSI"]

all_neighbours: List[Set[int]] = []

def get_row_len(prompt):
    while True:
        value = input(prompt)
        try:
            row_len = int(value)
        except ValueError:
            print("Your response must be an integer")
            continue
        if row_len <= 0:
            print("Your response must be positive")
            continue
        else:
            break
    return row_len


def make_board(row_len):
    board = []
    # Randomly select a die for (row_len * row_len) times
    for i in range(row_len ** 2):
        die = random.choice(dice)
        # For each die, randomly select a face and to the board
        letter = die[random.randrange(6)]
        board.append(letter)  
    return board


def print_board(board):
    print()
    row_len = math.sqrt(len(board))
    for i in range(len(board)):
        print(board[i] + " ", end = '')
        if i % row_len == row_len - 1:
            print()
    print()
            

def set_all_neighbours(board):
    """
    Generates a list of sets of neighbours for each position.
    
    For a 4x4 board, we number the positions:
        
         0  1  2  3
         4  5  6  7
         8  9 10 11
        12 13 14 15
    
    The neighbours of position 3 are 2, 6 and 7, while the neighbours of
    position 6 are 1, 2, 3, 5, 7, 9, 10, and 11.

    Parameters
    ----------
    board : list
        A list of (row_length * row_length) Boggle letters.
    """
    
    global all_neighbours
    row_len = math.sqrt(len(board))
    distances = [-row_len - 1, -row_len, -row_len + 1, -1, 1, row_len - 1, row_len, row_len + 1]
    
    for i in range(len(board)):
        neighbours_of_position = set()
        for d in distances:
            n = int(i + d)  # Neibhour's position
            n_col = n % row_len
            i_col = i % row_len
            if n >= 0 and n < len(board) and abs(i_col - n_col) <= 1:
                neighbours_of_position.add(n)  
        all_neighbours.append(neighbours_of_position)
        
    
def read_words(filename, dictionary, prefixes):
    """
    Load words from a file to a set and create a set of prefixes for those words

    Parameters
    ----------
    filename : str
        Name of the file to be read from.
    dictionary : set
        The set of possible words.
    prefixes : set
        The set of prefixes of possible words
    """

    with open(filename, 'r') as f:
        for index, word in enumerate(f):
            word = word.upper()
            dictionary.add(word.rstrip())
            for i in range(len(word)):
                prefixes.add(word[0:i])


def find_words(solutions, dictionary, prefixes, visited, board, start, prefix):
    """
    Visit each of the starting position's neighbours and add valid words to 
    solutions.
    
    Parameters
    ----------
    solutions : set
        The set of words found so far (which will be updated). 
    dictionary : set
        The set of possible words.
    prefixes : set
        The set of prefixes of possible words
    visited : list
        A list indicating for each position whether it's visited in this search.
    board : list
        A list of Boggle letters we're using in this game.
    start : int
        The position this search starts from.
    prefix : str
        Letters encountered so far in the current search.
    """
    
    # The position we're at is visited so we won't visit it again
    visited[start] = True
    
    # Prefix is initially empty so the candidate equals the starting letter
    candidate = prefix + board[start]
    if len(candidate) >= 3 and candidate in dictionary: # Found a valid word
        solutions.add(candidate)
    
    if candidate in prefixes:
        for n in all_neighbours[start]:  # Go through the neighbours of the position
            if not visited[n]:
                find_words(solutions, dictionary, prefixes, visited, board, n, candidate)
        
    visited[start] = False
    
    
def solve_boggle(board):
    """
    Solve a game of Boggle.

    Parameters
    ----------
    board : list
        The string array representing the game to solve.

    Returns
    -------
    list
        The list of words found.

    """
    
    dictionary = set()
    prefixes = set()
    
    read_words("dictionary.txt", dictionary, prefixes)
    
    solutions = set()
    visited = [False] * len(board)  # A boolean list, initially all False
   
    for i in range(len(board)):
        find_words(solutions, dictionary, prefixes, visited, board, i, "")
    
    return list(solutions)
    

def print_results(found, solutions):
    print("\nFound(%s):" % (len(found)))
    print('%s' % ', '.join(map(str, sorted(found))))
    missed = set(solutions) - found
    print("\nMissed(%s):" % (len(missed)))
    print('%s' % ', '.join(map(str, sorted(missed))))
    
    
def boggle(board, solutions):
    """
    Start up an interactive game of Boggle.
    
    Ask the user to supply one input per round and print the results after the
    user exits.

    Parameters
    ----------
    board : list
        A list of (row_length * row_length) Boggle letters.
    solutions : list
        A list of found Boggle Words.
    """
    
    found = set()  # The set of words found by the player
    while(True):
        word = input().upper()
        if word == "!EXIT":
            break;
        if word == "!PRINT":
            print_board(board)
            continue
        if word == "!CHEAT":
            print("\nSolutions(%s):" % (len(solutions)))
            print('%s\n' % ', '.join(map(str, sorted(solutions))))
            continue
        if word == "!HELP":
            print(
                "\nCommands:\n"
                "!print: prints the Boggle board\n"
                "!exit: exits the game\n"
                "!cheat: prints all the words on the Boggle board\n"
                "!help: prints this list of commands\n"
                )
            continue
        if word[0] == "!":
            print("Unknown command, type !help for a list of commands")
            continue
        if word in solutions:
            found.add(word)
        else:
            print("'%s' is not a valid word" % word)
    print_results(found, solutions)
            
        
def main():
    row_len = get_row_len("Please enter the length of the Boggle board: ")
    board = make_board(row_len)
    set_all_neighbours(board)  # Set up all neighbours before solving Boggle
    
    # Record the time taken to solve Boggle
    start = time.time()
    solutions = solve_boggle(board)
    end = time.time()
    print("Found %s words in %s seconds" % (len(solutions), round(end - start, 2)))
    
    print_board(board)
    boggle(board, solutions)  # Prompt the player for input until they exit
    

if __name__ == '__main__':
    main()
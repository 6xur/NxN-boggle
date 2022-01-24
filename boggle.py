import math, random, time
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
            print("'%s' is not a integer" % value)
            continue
        if row_len <= 0:
            print("Your response must be positive")
            continue
        else:
            break
    return row_len


def make_board(row_len):
    board = []
    # randomly select a die for row_len^2 times
    for i in range(row_len ** 2):
        die = random.choice(dice)
        # for each die, pick a random face and add it to the board
        char = die[random.randrange(6)]
        board.append(char)  
    return board


def print_board(board):
    row_len = math.sqrt(len(board))
    for i in range(len(board)):
        print(board[i] + " ", end = '')
        if i % row_len == row_len - 1:
            print();


def set_all_neighbours(board):
    global all_neighbours
    row_len = math.sqrt(len(board))
    distances = [-row_len - 1, -row_len, -row_len + 1, -1, 1, row_len - 1, row_len, row_len + 1]
    
    for i in range(len(board)):
        neighbours_of_position = set()
        for d in distances:
            n = int(i + d)  # neighbour's position
            n_col = n % row_len
            i_col = i % row_len
            if n >= 0 and n < len(board) and abs(i_col - n_col) <= 1:
                neighbours_of_position.add(n)  
        all_neighbours.append(neighbours_of_position)
        
    
def read_words(filename, dictionary):
    with open(filename, 'r') as f:
        for index, word in enumerate(f):
            word = word.upper()
            #TODO: for some reason bogglable never evaluates to true here, need to fix
            dictionary.add(word.rstrip())
                
        print("Read in %s words" % len(dictionary))


def find_words(solutions, dictionary, visited, board, start, prefix):
    # the position we're are is visited so we won't visit it again
    visited[start] = True
    
    # prefix is initially empity so the candidate is the starting letter
    candidate = prefix + board[start]
    if len(candidate) >= 3 and candidate in dictionary: # found a valid word
        solutions.add(candidate)
    
    # go through all the neighbours of the start position
    for n in all_neighbours[start]:
        if not visited[n]:
            find_words(solutions, dictionary, visited, board, n, candidate)
        
    visited[start] = False
    
    
def solve_boggle(board):
    dictionary = set()
    read_words("dictionary.txt", dictionary)
    solutions = set()
    visited = [False] * len(board)  # a boolean list, initially all false
    for i in range(len(board)):
        find_words(solutions, dictionary, visited, board, i, "")
    
    return list(solutions)
    

def main():
    row_len = get_row_len("Please enter the row length: ")
    print()
    board = make_board(row_len)
    print_board(board)
    print()
    set_all_neighbours(board)
    
    start = time.time()
    solutions = solve_boggle(board)
    stop = time.time()
    print("time taken: %s seconds" % (stop - start))
    print(solutions)


if __name__ == '__main__':
    main()
import math, random, sys, time
from typing import List, Set


dice = ["AJBBOO","AFFPSK","ANEAGE","APSHCO", 
        "QNUMHI","ZNHRLN","TDSTYI","TTWOOA",
        "TLRYET","TUMIOC","EDVLRY","EDRLXI",
        "EEGNHW","EIOTSS","ERHTWV","EENUSI"]

row_len = int(math.sqrt(len(dice)))  # should be 4 because we have 16 dice

all_neighbours: List[Set[int]] = []
#distances = [-5, -4, -3, -1, 1, 3, 4, 5]
distances = [-1 - row_len, -row_len, 1 - row_len, -1, 1, row_len - 1, row_len, row_len + 1]
for i in range(len(dice)):
    neighbours_of_position = set()
    for d in distances:
        n = i + d  # neighbour's position
        n_col = n % row_len
        i_col = i % row_len
        if n >= 0 and n < len(dice) and abs(i_col - n_col) <= 1:
            neighbours_of_position.add(n)  
    all_neighbours.append(neighbours_of_position)


def print_board(board):
    for i in range(len(board)):
        print(board[i] + " ", end = '')
        if i % row_len == row_len - 1:
            print();
            

def shake(dice):
    board = []
    random.shuffle(dice)
    for die in dice:
        letter = die[random.randrange(6)]
        board.append(letter)  
    return board


def find_words(solutions, dictionary, visited, board, start, prefix):
    # the position we're are is visited so we won't visit it again
    visited[start] = True
    
    # prefix is initially empity so the candidate is the starting letter
    candidate = prefix + board[start]
    if len(candidate) >= 3 and candidate in dictionary: # found a real word
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
    visited = [False] * len(dice)  # a boolean list, initially all false
    
    for i in range(len(dice)):
        find_words(solutions, dictionary, visited, board, i, "")
    
    return list(solutions)


def read_words(filename, dictionary):
    with open(filename, 'r') as f:
        for index, word in enumerate(f):
            word = word.upper()
            dictionary.add(word.rstrip())
        print("Read in %s words" % len(dictionary))
        
       
def print_results(found, solutions):
    print("\nFound(%s):" % (len(found)))
    print('%s' % ', '.join(map(str, sorted(found))))
    missed = set(solutions) - found
    print("\nMissed(%s):" % (len(missed)))
    print('%s' % ', '.join(map(str, sorted(missed))))
    
    
def main():
    board = shake(dice)
    print_board(board)
    
    start = time.time()
    solutions = solve_boggle(board)
    stop = time.time()
    print("time taken: %s" % (stop - start))
    
    found = set()
    
    while(True):
        word = input().upper()
        if word == "Q":
            break;
        if word in solutions:
            found.add(word)
        else:
            print("'%s' is not a valid word" % word)
            
    print_results(found, solutions)
    
    
if __name__ == '__main__':
  main()
import math, random


dice = ["AJBBOO","AFFPSK","ANEAGE","APSHCO","QNUMHI","ZNHRLN","TDSTYI","TTWOOA","TLRYET","TUMIOC","EDVLRY","EDRLXI","EEGNHW","EIOTSS","ERHTWV","EENUSI"]

TESTBOARD = ['R', 'H', 'R', 'E',
             'Y', 'P', 'C', 'S', 
             'W', 'N', 'S', 'N',
             'T', 'E', 'G', 'O']

ROW_LEN = math.sqrt(len(dice))  # Should be 4 because we have 16 dice

neighbours = []  # list of sets of neighbours
distance = [-5, -4, -3, -1, 1, 3, 4, 5]
for i in range(len(dice)):
    die = set()
    for d in distance:
        n = i + d  # neighbour's position
        nCol = n % ROW_LEN
        iCol = i % ROW_LEN
        if n >= 0 and n < len(dice) and abs(iCol - nCol) <= 1:
            die.add(n)
            
    neighbours.append(die)


def printBoard(board):
    for i in range(len(board)):
        print(board[i], end = '')
        if i % ROW_LEN == ROW_LEN - 1:
            print();
            

def shake(dice):
    board = []
    random.shuffle(dice)
    for die in dice:
        randFace = die[random.randrange(6)]
        board.append(randFace)  
    return board


def findWords(boggleWords, words, used, board, start, prefix):
    used[start] = True  # the place we're at is used so we won't visit it again
    
    candidate = prefix + board[start]  # prefix is empty initially, so our candidate word is the starting letter
    if len(candidate) >= 3 and candidate in words:  # found a real word
        boggleWords.add(candidate)
        #print("found one")
    
    # loop through all the neighbours of the start position
    for n in neighbours[start]:
        if not used[n]:
            findWords(boggleWords, words, used, board, n, candidate)
        
    used[start] = False

    
def solveBoggle(board):
    words = set()
    readWords("dictionary.txt", words)
    
    boggleWords = set()  # the words we've found
    used = [False] * len(dice)  # a boolean list of size 16, initially all false
    
    for i in range(len(dice)):
        findWords(boggleWords, words, used, board, i, "")
    
    return list(boggleWords)


def readWords(filename, words):
    with open(filename, 'r') as f:
        for index, value in enumerate(f):
            word = value.upper()
            words.add(word.rstrip())
        print("Read in " + str(index + 1) + " words, making a word set of size " + str(len(words)))
        #print(words)
        
        
def main():
    board = shake(dice)
    printBoard(board)
    
    solution = solveBoggle(board)
    
    print("Found " + str(len(solution)))
    print(solution)
    
if __name__ == '__main__':
  main()
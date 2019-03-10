import copy

class Problem():


    def problemInfo(self):
        print("Sudoku Problem\n")

    def __init__(self):

        self.table =  [[3, 1, 4, 2, 5, 6],
                       [2, 0, 5, 1, 3, 4],
                       [1, 0, 3, 0, 6, 5],
                       [5, 4, 6, 3, 0, 0],
                       [4, 5, 1, 6, 0, 3],
                       [6, 3, 0, 5, 4, 1]]

        self.size = len(self.table)
        self.squareSize = int(self.size/3)
        self.problemInfo()

    def addToTheBoard(self, state, newEntry):
        value, row, column = newEntry[0], newEntry[1], newEntry[2]
        newBoard = copy.deepcopy(state)
        newBoard[row][column] = value
        return newBoard

    def getUnusedValues(self, values, used):
        return [number for number in values if number not in used]

    def getFirstEmpty(self, board, state):
        for row in range(board):
            for column in range(board):
                if state[row][column] == 0:
                    return row, column


    def simpleSolving(self, state):
        allowedNumbers = range(1, self.size + 1)
        row, column = self.getFirstEmpty(self.size, state)

        for number in allowedNumbers:
            yield number, row, column


    def greedySolving(self, state):
        allowedNumbers = range(1, self.size + 1)
        validInCol = []
        validInRow = []
        validInSquare = []

        row, column = self.getFirstEmpty(self.size, state)

        for rowIndex in range(self.size):
            if state[row][rowIndex] != 0:
                validInRow.append(state[row][rowIndex])
        allowed = self.getUnusedValues(allowedNumbers, validInRow)


        for colIndex in range(self.size):
            if state[colIndex][column] != 0:
                validInCol.append(state[colIndex][column])
        allowed = self.getUnusedValues(allowed, validInCol)

        rStart = int(row / self.squareSize) * self.squareSize
        cStart = int(column / 3) * 3

        for squareRow in range(0, self.squareSize):
            for squareCol in range(0, 3):
                validInSquare.append(state[rStart + squareRow][cStart + squareCol])
        allowed = self.getUnusedValues(allowed, validInSquare)

        for number in allowed:
            yield number, row, column


    def checkIfSolution(self, state):

        desiredSum = sum(range(1, self.size + 1))

        for row in range(self.size):
            if sum(state[row]) != desiredSum:
                return False

            colSum = 0
            for column in range(self.size):
                colSum += state[column][row]

            if colSum != desiredSum:
                return False

        for column in range(0, self.size, 3):
            for row in range(0, self.size, self.squareSize):

                squareSum = 0
                for squareRow in range(0, self.squareSize):
                    for squareCol in range(0, 3):
                        squareSum += state[row + squareRow][column + squareCol]

                if squareSum != desiredSum:
                    return False

        return True
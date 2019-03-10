class State:

    def __init__(self, state, newEntry = None):
        self.state = state
        self.newEntry = newEntry

    def simpleExpand(self, problem):
        return [self.getNewNode(problem, newEntry)
                for newEntry in problem.simpleSolving(self.state)]

    def greedyExpand(self, problem):
        return [self.getNewNode(problem, newEntry)
                for newEntry in problem.greedySolving(self.state)]

    def getNewNode(self, problem, newEntry):
        return State(problem.addToTheBoard(self.state, newEntry), newEntry)

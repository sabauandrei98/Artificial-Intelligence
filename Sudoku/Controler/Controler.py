from queue import Queue
from State.State import State

class Controler:

    def BFS(self, problem, type):

        startNode = State(problem.table)
        if problem.checkIfSolution(startNode.state):
            return startNode

        q = Queue()
        q.put(startNode)

        while (q.qsize() != 0):
            node = q.get()

            if type == "simple":
                for neighbour in node.simpleExpand(problem):
                    if problem.checkIfSolution(neighbour.state):
                        return neighbour
                    q.put(neighbour)
            else:
                if type == "greedy":
                    for neighbour in node.greedyExpand(problem):
                        if problem.checkIfSolution(neighbour.state):
                            return neighbour
                        q.put(neighbour)
        return None

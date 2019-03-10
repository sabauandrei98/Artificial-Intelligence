import time
from Controler.Controler import Controler
from Problem.Problem import Problem

class UI:

    def printUI(self):
        print("Problem solver\n")
        print("1. BFS")
        print("2. GBFS")

    def run(self):

        self.printUI()

        while True:
            cmd = input (">>")

            if cmd == "1":
                self.solve("simple")

            if cmd == "2":
                self.solve("greedy")


    def solve(self, type):
        start = time.time()

        problem = Problem()
        controler = Controler()
        result = controler.BFS(problem, type)
        totalTime = time.time() - start

        if result:
            for row in result.state:
                print(row)
        else:
            print("No solution")

        print("Total time: " + str(totalTime))





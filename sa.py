from __future__ import division
import tsplib95
from satsp import solver

problem = tsplib95.load("berlin52.tsp.txt")

print("Parsing...")
G = problem.get_graph()
p = []
n = list(G.edges)
x = 1
for i in n:
    y = list(i)
    y.insert(0, x)
    p.append(y)
    x += 1

print("Finished Parsing\nNow Annealing...")

solver.Solve(p, None, #Coordinates and Adjacency Matrix - Adj Matrix calculated at runtime
            start_temp = 100, stop_temp = 30, #Starting and Stopping temp automatically defined
            alpha = 0.19, epochs = 5000,    #Cooling rate and Epoch amount - Epochs calculated in relation to stop_temp and alpha
            epoch_length = 3, epoch_length_factor = 1.09, #Number of iterations per epoch, and epoch length increasion rate
            stopping_count=100, screen_output = True) #Number of epochs where no improvement is made
solver.PrintSolution()


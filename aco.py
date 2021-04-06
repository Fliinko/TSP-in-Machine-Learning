from __future__ import division
import tsplib95
import acopy
import matplotlib.pyplot as plt
import networkx as nx


problem = tsplib95.load("brg180.tsp.txt")

G = problem.get_graph()
p = []
n = list(G.edges)
x = 1
for i in n:
    y = list(i)
    y.insert(0, x)
    p.append(y)
    x += 1

solver = acopy.Solver(rho=.03, q=1)
colony = acopy.Colony(alpha=1, beta=3)
tour = solver.solve(G, colony, limit=1000)
print(tour.cost)
#print(tour.best)
print(tour.path)

# Printing
colors = ['black', 'blue']
plt.figure(dpi=300)
_, ax = plt.subplots()
pos = problem.display_data or problem.node_coords
nx.draw_networkx_nodes(G, pos=pos, ax=ax, node_color=(0.4157, 0.3529, 0.3490))
nx.draw_networkx_labels(G, pos=pos, labels={i: str(i) for i in range(1, len(G.nodes) + 1)}, font_size=8,
                        font_color='white')
solution = tour.path
path = solution
nx.draw_networkx_edges(G, pos=pos, edgelist=path, edge_color=colors[0])
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.show()
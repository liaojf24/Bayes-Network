import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import  pandas  as pd
import get_chi_donor as pre

nodes=np.zeros(18)
for i in range(18):
    nodes[i]=int(i-9)
G=nx.Graph()
#G.add_node('-9')
G.add_nodes_from(nodes)
chart=pre.dependence_chart
for j in range(18):
    for k in range(j,18):
        if chart[j,k]:
            G.add_edge(j-9,k-9)

nx.draw(G,with_labels=True)
plt.show()


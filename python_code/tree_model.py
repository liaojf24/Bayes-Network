from collections import defaultdict
from heapq import heapify, heappush, heappop
from get_chi_donor import dependence_chart
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import  pandas  as pd



##create a tree containing all the edges
def get_all_edges(chart):
    node=list()
    tree=list()
    len=chart.shape[0]#the row numbers of chart
    for i in range(len):
        for j in range(i+1,len):
            if chart[i,j]:
                node=[str(i-9),str(j-9),chart[i,j]]

                tree.append(node)
    return(tree)


def Prim(nodes, edges):
    '''  基于最小堆实现的Prim算法  '''
    element = defaultdict(list)
    for start, stop, weight in edges:
        element[start].append((weight, start, stop))
        element[stop].append((weight, stop, start))
    all_nodes = set(nodes)
    #used_nodes = set(nodes[0]) ???why use set(nodes),cause -9—— -3 duplicate
    used_nodes=list()
    used_nodes.append(nodes[0])

    usable_edges = element[nodes[0]][:]
    heapify(usable_edges)
    # 建立最小堆
    MST = []
    while usable_edges and (all_nodes - set(used_nodes)):
        weight, start, stop = heappop(usable_edges)
        if stop not in used_nodes:
            used_nodes.append(stop)
            MST.append((start, stop, weight))
            for member in element[stop]:
                if member[2] not in used_nodes:
                    heappush(usable_edges, member)
    return MST


# def main():
#     nodes=list(range(18))
#     edges = get_all_edges(dependence_chart)
#     print("\n\nThe undirected graph is :", edges)
#     print("\n\nThe minimum spanning tree by Prim is : ")
#     print(Prim(nodes, edges))
#
#
# if __name__ == '__main__':
#     main()

#def main():
G = nx.Graph()
nodes = ['-9', '-8', '-7', '-6', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5', '6', '7', '8']
G.add_nodes_from(nodes)
edges = get_all_edges(dependence_chart)
MST=Prim(nodes,edges)

# if __name__=='__main__':
#     main()

    # for nodes in MST:
    #     G.add_edge(nodes[0],nodes[1])
    # nx.draw(G, with_labels=True)
    # plt.show()

# if __name__ == '__main__':
#     main()
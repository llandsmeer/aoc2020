import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def normalize_name(x):
    a = x.split()
    if 'bag' in a[-1]: del a[-1]
    if a[0].isdigit(): del a[0]
    return '_'.join(a)

def get_count(x):
    if x == 'no other bags': return 0
    a = x.split()
    if a[0].isdigit():
        return int(a[0])
    return 1

def nbags(G, n):
    total = 1
    for parent in G.predecessors(n):
        total += G.edges[(parent,n)]['count'] * nbags(G, parent)
    return total

def read_graph(filename):
    G = nx.DiGraph()
    for line in open(filename):
        parent, childs_ = line.rstrip('.\n').split('contain')
        parent = normalize_name(parent.strip())
        childs = [child.strip() for child in childs_.split(', ')]
        G.add_node(parent)
        for child in childs:
            G.add_edge(normalize_name(child), parent, count=get_count(child))
    return G

G = read_graph('./aoc7.in')

reachable = nx.algorithms.dag.descendants(G, 'shiny_gold')
ancestors = nx.algorithms.dag.ancestors(G, 'shiny_gold')

print(len(reachable))
print(nbags(G, 'shiny_gold') - 1)

colors = ['gold' if node in reachable else 'blue' if node in ancestors else 'red' for node in G.nodes]
nx.draw_spring(G, with_labels=True, node_color=colors)
plt.show()

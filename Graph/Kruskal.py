#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def get_nid(node, nid):
    while (node != nid[node]):
        node = nid[node]
    return node
        

def kruskals(g_nodes, g_from, g_to, g_weight):
    res = 0
    edges = sorted([e for e in zip(g_from, g_to, g_weight)], key=lambda k: k[2])
    nid = [i for i in range(g_nodes + 1)]
    
    for edge in edges:
        from_nid = get_nid(edge[0], nid)
        to_nid = get_nid(edge[1], nid)
        weight = edge[2]
        if from_nid != to_nid:
            res += weight
            nid[to_nid] = nid[from_nid]
    
    return res

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)
    print(res)
    # Write your code here.

    # fptr.close()

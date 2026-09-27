import numpy as np
from graph import Graph, Node, Edge

def readFile(filepath: str):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        return lines

def buildGraph(filepath: str):
    lines = readFile(filepath)
    nodes = loadNodesFromFile(lines)
    adjacencyMatrix = loadAdjacencyMatrixFromFile(lines)
    edges = loadEdgesFromAdjacencyMatrix(adjacencyMatrix, nodes)
    isDirected = isDirectedVerification(adjacencyMatrix)
    graph = Graph(nodes, edges, adjacencyMatrix, isDirected)
    return graph

def loadNodesFromFile(lines: list[str]):
    header = lines[0].split()
    nodes = [Node(label) for label in header]
    return nodes

def loadAdjacencyMatrixFromFile(lines: list[str]):
    matrixRows = []
    for line in lines[1:]:
        values = line.split()[1:]
        matrixRows.append([float(value) for value in values])
    adjacencyMatrix = np.array(matrixRows)
    return adjacencyMatrix

def loadEdgesFromAdjacencyMatrix(adjacencyMatrix: np.ndarray, nodes: list[Node]):
    edges = []
    n = adjacencyMatrix.shape[0]
    for i in range(n):
        for j in range(n):
            if adjacencyMatrix[i,j] != 0:
                edges.append(Edge(nodes[i],nodes[j],adjacencyMatrix[i,j]))
    return edges

def isDirectedVerification(adjacencyMatrix: np.ndarray):
    n = adjacencyMatrix.shape[0]
    for i in range(n):
        for j in range(n):
            if adjacencyMatrix[i,j] != adjacencyMatrix[j,i]:
                return True
    return False


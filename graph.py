#Definition of a graph in sapanish G=(V,A), in english G=(V,E)

from dataclasses import dataclass, field
from email import header
from platform import node
from matplotlib import lines
import numpy as np

#Clase abstracta de grafo
#Grafo Posible: 
#Dirigido, No Ponderado
#Dirigido, Ponderado
#No Dirigido, No Ponderado
#No Dirigido, Ponderado

#1.Clase Vértice
@dataclass(frozen=True)
class Node:
    name: str = ""

#2.Clase Arista
@dataclass
class Edge:
    source: Node
    target: Node
    weight: float = 1.0


#3. CLase Grafo
@dataclass
class Graph():
    nodes: list[Node] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)
    adjacencyMatrix: np.ndarray = field(default_factory=lambda: np.array([]))
    isDirected: bool = False

    def addNode(self,newNode : Node):
        self.nodes.append(newNode)

    def addEdge(self, newEdge : Edge):
        self.edges.append(newEdge) 

    def printNodes(self):
        print("Nodes:")
        for node in self.nodes:
            print(node.name)

    def printEdges(self):
        print("Edges:")
        for edge in self.edges:
            print(f"({edge.source.name},{edge.target.name}, weight: {edge.weight})")

    def printGraph(self):
        print(f"Nodes: {len(self.nodes)}, Aristas: {len(self.edges)}, Directed:", "yes" if self.isDirected else "no")
        self.printNodes()
        self.printEdges()

    def nodesToString(self):
        lines = ["Nodes:"]
        for node in self.nodes:
            lines.append(node.name)
        return "\n".join(lines)

    def edgesToString(self):
        lines = ["Edges:"]
        for edge in self.edges:
            lines.append(f"({edge.source.name}, {edge.target.name}, {edge.weight})")
        return "\n".join(lines)
    
    def adjacencyMatrixToString(self):
        header = "     " + "  ".join(node.name for node in self.nodes)
        rows = [header]
        for i, node in enumerate(self.nodes):
            row = "  ".join(f"{val:.1f}" for val in self.adjacencyMatrix[i])
            rows.append(f"{node.name}:  {row}")
        return "\n".join(rows)

    def graphInfo(self):
        header = f"Nodes: {len(self.nodes)}, Edges: {len(self.edges)}, Directed: {'yes' if self.isDirected else 'no'}"
        return "\n\n".join([header, self.matrixToString(), self.nodesToString(), self.edgesToString()])

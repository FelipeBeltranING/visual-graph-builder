#Definition of a graph in sapanish G=(V,A), in english G=(V,E)

from dataclasses import dataclass, field
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

    def printGraph(self):
        print(f"Nodes: {len(self.graph.nodes)}, Aristas: {len(self.graph.edges)}, Directed:", "yes" if self.graph.isDirected else "no")
        print("Nodes:")
        for node in self.nodes:
            print(node.name)
        print("Edges:")
        for edge in self.edges:
            print(f"({edge.source.name},{edge.target.name}, weight: {edge.weight}")

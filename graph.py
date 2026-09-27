#Definición de un grafo G=(V,A), en ingles G=(V,E)

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
    id: str
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
    node: list[Node] = field(default_factory=list)
    edge: list[Edge] = field(default_factory=list)
    adjacencyMatrix: np.ndarray = field(default_factory=lambda: np.array([]))
    isDirected: bool = False

    def addNode(self,newNode : Node):
        self.node.append(newNode)

    def addEdge(self, newEdge : Edge):
        self.edge.append(newEdge)
        
    def createAdjacencyMatrix(self):
        matrixSize = len(self.node)
        self.adjacencyMatrix = np.zeros((matrixSize,matrixSize))
        for edge in self.edge:
            i = self.node.index(edge.source)
            j = self.node.index(edge.target)
            self.adjacencyMatrix[i,j] = edge.weight
                   

  

#Definition of a graph in sapanish G=(V,A), in english G=(V,E)

from dataclasses import dataclass, field
from email import header
from platform import node
import queue
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
    
    def adjacentTo(self, node):
        """Nodos w tales que existe arista <node, w>"""
        return [edge.target for edge in self.edges if edge.source == node]

    def adjacentFrom(self, node):
        """Nodos u tales que existe arista <u, node>"""
        return [edge.source for edge in self.edges if edge.target == node]
    
    def findPath(self, start, end):
        visited = {start}
        queue = [[start]]          # cada elemento es un camino parcial (lista de nodos)
    
        while queue:
            path = queue.pop(0)
            current = path[-1]
        
            if current == end:
                return path
        
        for neighbor in self.adjacentTo(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    
        return None   # no existe camino
    
    def hasCycleUndirected(self):
        visited = set()
    
        def dfs(node, parent):
            visited.add(node)
            for neighbor in self.adjacentTo(node):
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False
    
        for node in self.nodes:
            if node not in visited:
                if dfs(node, None):
                    return True
        return False

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

    def matrixToString(self):
        header = "      " + "  ".join(f"{node.name:>4}" for node in self.nodes)
        rows = [header]
        for i, node in enumerate(self.nodes):
            row = "  ".join(f"{val:>4.1f}" for val in self.adjacencyMatrix[i])
            rows.append(f"{node.name:>4}  {row}")
        return "\n".join(rows)

    def graphInfo(self):
        header = f"Nodes: {len(self.nodes)}, Edges: {len(self.edges)}, Directed: {'yes' if self.isDirected else 'no'}"
        return "\n\n".join([header, self.matrixToString(), self.nodesToString(), self.edgesToString()])


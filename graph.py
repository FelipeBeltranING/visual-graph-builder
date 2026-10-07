#Definition of a graph in sapanish G=(V,A), in english G=(V,E)

from dataclasses import dataclass, field
from email import header
from os import path
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
    
    def dijkstra(self, start, end):
        distances = {node: float('inf') for node in self.nodes}
        previous = {node: None for node in self.nodes}
        distances[start] = 0
        unvisited = set(self.nodes)

        while unvisited:
            current = min(unvisited, key=lambda node: distances[node])
            unvisited.remove(current)

            if current == end:
                break
            if distances[current] == float('inf'):
                break   # los nodos restantes son inalcanzables

            for edge in self.edges:
                if edge.source == current and edge.target in unvisited:
                    newDist = distances[current] + edge.weight
                    if newDist < distances[edge.target]:
                        distances[edge.target] = newDist
                        previous[edge.target] = current

        return self._reconstructPath(previous, start, end), distances[end]
    
    def _reconstructPath(self, previous, start, end):
        if previous[end] is None and end != start:
            return None   # no hay camino
    
        path = [end]
        while path[-1] != start:
            path.append(previous[path[-1]])
        path.reverse()
        return path
    
    def bellmanFord(self, start, end):
        distances = {node: float('inf') for node in self.nodes}
        previous = {node: None for node in self.nodes}
        distances[start] = 0
    
        n = len(self.nodes)
        for _ in range(n - 1):
            for edge in self.edges:
                if distances[edge.source] + edge.weight < distances[edge.target]:
                    distances[edge.target] = distances[edge.source] + edge.weight
                    previous[edge.target] = edge.source

    # una iteración extra para detectar ciclos de peso negativo
        for edge in self.edges:
            if distances[edge.source] + edge.weight < distances[edge.target]:
                raise ValueError("El grafo tiene un ciclo de peso negativo")

        return self._reconstructPath(previous, start, end), distances[end]
    
    def conceptsToString(self):
        lines = ["Nodos adyacentes:"]
        for node in self.nodes:
            adj = ", ".join(n.name for n in self.adjacentTo(node))
            lines.append(f"  {node.name} -> [{adj}]")
    
        lines.append(f"\n¿Tiene ciclo? {'Sí' if self.hasCycle() else 'No'}")
    
        if len(self.nodes) >= 2:
            path = self.findPath(self.nodes[0], self.nodes[-1])
            if path:
                pathStr = " -> ".join(n.name for n in path)
                lines.append(f"Camino de {self.nodes[0].name} a {self.nodes[-1].name}: {pathStr}")
            else:
                lines.append(f"No hay camino de {self.nodes[0].name} a {self.nodes[-1].name}")
    
        return "\n".join(lines)

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


from cProfile import label
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

from matplotlib import container
from matplotlib.pyplot import title
import graphBuilder
import graphVisualizer

class App:
    def __init__(self, root):
        self.root = root
        self.graph = None
        self.filepath = None

        root.title("Graph Builder")
        root.geometry("2048x1080")

        self.createLayout()
        self.createButtons()
        self.createTextBox()

    def createLayout(self):
        self.topFrame = tk.Frame(self.root)
        self.topFrame.pack(side="top", fill="x", pady=10)

        self.bottomFrame = tk.Frame(self.root)
        self.bottomFrame.pack(side="bottom", fill="both", expand=True)

        self.bottomFrame.columnconfigure(0, weight=1)
        self.bottomFrame.columnconfigure(1, weight=1)
        self.bottomFrame.columnconfigure(2, weight=1)
        self.bottomFrame.columnconfigure(3, weight=1)
        self.bottomFrame.rowconfigure(0, weight=1)

        self.leftFrame = tk.Frame(self.bottomFrame)
        self.leftFrame.grid(row=0, column=0, sticky="nsew")

        self.originalGraphFrame = self._makeGraphPanel(self.bottomFrame, "Grafo original", col=1)
        self.dijkstraFrame = self._makeGraphPanel(self.bottomFrame, "Dijkstra", col=2)
        self.bellmanFrame = self._makeGraphPanel(self.bottomFrame, "Bellman-Ford", col=3)

    def _makeGraphPanel(self, parent, title, col):
        container = tk.Frame(parent)
        container.grid(row=0, column=col, sticky="nsew")

        label = tk.Label(container, text=title, font=("Segoe UI", 11, "bold"))
        label.pack(side="top", pady=5)

        canvasFrame = tk.Frame(container)
        canvasFrame.pack(fill="both", expand=True)

        return canvasFrame   # este es el frame donde se dibuja el grafo

    def createButtons(self):
        buttonFrame = tk.Frame(self.topFrame)
        buttonFrame.pack()

        self.uploadButton = tk.Button(buttonFrame, text="Upload Graph File", width=18, height=2, font=("Segoe UI", 14, "bold"), bg="#2d7ff9", fg="white", command=self.uploadMatrix)
        self.uploadButton.pack(side="left", padx=10)

        tk.Label(buttonFrame, text="Origen:", font=("Segoe UI", 12)).pack(side="left", padx=(20, 5))
        self.originEntry = tk.Entry(buttonFrame, width=8, font=("Segoe UI", 12))
        self.originEntry.pack(side="left")

        tk.Label(buttonFrame, text="Destino:", font=("Segoe UI", 12)).pack(side="left", padx=(10, 5))
        self.destEntry = tk.Entry(buttonFrame, width=8, font=("Segoe UI", 12))
        self.destEntry.pack(side="left")

        self.dijkstraButton = tk.Button(buttonFrame, text="Dijkstra", width=12, height=2, font=("Segoe UI", 12, "bold"), bg="#28a745", fg="white", command=self.runDijkstra)
        self.dijkstraButton.pack(side="left", padx=10)

        self.bellmanButton = tk.Button(buttonFrame, text="Bellman-Ford", width=12, height=2, font=("Segoe UI", 12, "bold"), bg="#ff8c00", fg="white", command=self.runBellmanFord)
        self.bellmanButton.pack(side="left", padx=10)

    def createTextBox(self):
        tk.Label(self.leftFrame, text="Información del grafo", font=("Segoe UI", 12, "bold")).pack(pady=(10, 0))
        self.txtInfo = scrolledtext.ScrolledText(
            self.leftFrame, width=50, height=22, font=("Segoe UI", 12)
        )
        self.txtInfo.pack(padx=10, pady=5)

        tk.Label(self.leftFrame, text="Resultado del algoritmo", font=("Segoe UI", 12, "bold")).pack(pady=(10, 0))
        self.txtResult = scrolledtext.ScrolledText(
            self.leftFrame, width=50, height=6, font=("Segoe UI", 12)
        )
        self.txtResult.pack(padx=10, pady=5)

    def findNodeByName(self, name):
        for node in self.graph.nodes:
            if node.name == name:
                return node
        return None
    
    def loadGraph(self, filepath: str):
        try:
            self.graph = graphBuilder.buildGraph(filepath)
            graphVisualizer.drawGraph(self.graph, self.originalGraphFrame)
            self.showGraphInfo()
        except ValueError as e:
            self.showText(f"Error al cargar el archivo:\n{e}")

    def runDijkstra(self):
        self._runShortestPath(self.graph.dijkstra, "Dijkstra", self.dijkstraFrame)

    def runBellmanFord(self):
        self._runShortestPath(self.graph.bellmanFord, "Bellman-Ford", self.bellmanFrame)  # si agregas el 3er panel

    def _runShortestPath(self, algorithm, algorithmName, targetFrame):
        if not self.graph:
            self.showResult("Primero carga un grafo.")
            return

        startName = self.originEntry.get().strip()
        endName = self.destEntry.get().strip()
        start = self.findNodeByName(startName)
        end = self.findNodeByName(endName)

        if not start or not end:
            self.showResult(f"Nodo origen o destino inválido. Nodos disponibles: {[n.name for n in self.graph.nodes]}")
            return

        try:
            path, cost = algorithm(start, end)
        except ValueError as e:
            self.showResult(str(e))
            return

        if path is None:
            self.showResult(f"No existe camino de {startName} a {endName}.")
            return

        pathStr = " -> ".join(n.name for n in path)
        self.showResult(f"{algorithmName}\nRuta: {pathStr}\nCosto total: {cost}")
        graphVisualizer.drawGraph(self.graph, targetFrame, highlightPath=path)

    
    def uploadMatrix(self):
        self.filepath = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("Text files", "*.txt")]
        )
        if self.filepath:
            self.loadGraph(self.filepath)
        else:
            print("No file selected.")

    def showGraphInfo(self):
        if self.graph:
            self.showText(self.graph.graphInfo())

    def showText(self, text: str):
        self.txtInfo.config(state="normal")
        self.txtInfo.delete(1.0, tk.END)
        self.txtInfo.insert(tk.END, text)
        self.txtInfo.config(state="disabled")

    def showResult(self, text: str):
        self.txtResult.config(state="normal")
        self.txtResult.delete(1.0, tk.END)
        self.txtResult.insert(tk.END, text)
        self.txtResult.config(state="disabled")    

root = tk.Tk()
app = App(root)
root.mainloop()
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
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
        self.topFrame.pack(side="top", fill="x",pady=10)

        self.bottomFrame = tk.Frame(self.root)
        self.bottomFrame.pack(side="bottom", fill="both", expand=True)
        
        self.bottomFrame.columnconfigure(0, weight=1)
        self.bottomFrame.columnconfigure(1, weight=1)
        self.bottomFrame.rowconfigure(0, weight=1)

        self.leftFrame = tk.Frame(self.bottomFrame)
        self.leftFrame.grid(row=0, column=0, sticky="nsew")

        self.rightFrame = tk.Frame(self.bottomFrame)
        self.rightFrame.grid(row=0, column=1, sticky="nsew")

    def createButtons(self):
        buttonFrame = tk.Frame(self.topFrame)
        buttonFrame.pack()
        self.uploadButton = tk.Button(buttonFrame, text="Upload Graph File",width=20, height=2, font=("Segoe UI", 14, "bold"),bg="#2d7ff9", fg="white", command=self.uploadMatrix)
        self.uploadButton.pack(side="left", padx=10)

    def createTextBox(self):
        self.txtInfo = scrolledtext.ScrolledText(
            self.leftFrame, width=50, height=30, font=("Segoe UI", 15)
            )
        self.txtInfo.pack(padx=10, pady=10)
    
    def uploadMatrix(self):
        self.filepath = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("Text files", "*.txt")]
        )
        if self.filepath:
            self.loadGraph(self.filepath)
        else:
            print("No file selected.")

    def loadGraph(self, filepath: str):
        try:
            self.graph = graphBuilder.buildGraph(filepath)
            graphVisualizer.drawGraph(self.graph, self.rightFrame)
            self.showGraphInfo()
        except ValueError as e:
            self.showText(f"Error al cargar el archivo:\n{e}")

    def showGraphInfo(self):
        if self.graph:
            self.graph.printGraph()
            self.showText(self.graph.graphInfo())

    def showText(self, text: str):
        self.txtInfo.config(state="normal")
        self.txtInfo.delete(1.0, tk.END)
        self.txtInfo.insert(tk.END, text)
        self.txtInfo.config(state="disabled")

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
        

root = tk.Tk()
app = App(root)
root.mainloop()
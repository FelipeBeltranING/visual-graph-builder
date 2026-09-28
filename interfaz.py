import tkinter as tk
from tkinter import filedialog
import graphBuilder

class App:
    def __init__(self, root):
        self.root = root
        self.graph = None
        self.filepath = None

        root.title("Graph Builder")
        root.geometry("1920x1080")

        self.createButtons()
            
    def createButtons(self):
        self.uploadButton = tk.Button(self.root, text="Upload Graph File",width=20, height=2,  font=("Segoe UI", 14, "bold"),bg="#2d7ff9", fg="white", command=self.uploadMatrix)
        self.uploadButton.pack(pady=10)

        self.showInfoButton = tk.Button(self.root, text="Show Graph Info",width=20, height=2,  font=("Segoe UI", 14, "bold"),bg="#2d7ff9", fg="white", command=self.showGraphInfo)
        self.showInfoButton.pack(pady=10)
     
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
        self.graph = graphBuilder.buildGraph(filepath)
        print("Graph loaded successfully.")

    def showGraphInfo(self):
        if self.graph:
            self.graph.printGraph()

root = tk.Tk()
app = App(root)
root.mainloop()
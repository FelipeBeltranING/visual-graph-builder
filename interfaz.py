import tkinter as tk
from tkinter import filedialog
import graphBuilder 

class App:
    def __init__(self, root):
        self.graph = None
        self.filepath = None
        root.title("Graph Builder")

        btnCargar = tk.Button(root, text="Upload Matrix", command=self.uploadMatrix)
        btnCargar.pack(pady=20)

        btnInfo = tk.Button(root, text="Show Graph Info", command=self.showGraphInfo)
        btnInfo.pack(pady=20)

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

    



root = tk.Tk()

root.mainloop()
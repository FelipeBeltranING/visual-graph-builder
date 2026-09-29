import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
import graphBuilder

class App:
    def __init__(self, root):
        self.root = root
        self.graph = None
        self.filepath = None

        root.title("Graph Builder")
        root.geometry("1920x1080")

        self.createLayout()
        self.createButtons()
        self.createTextBox()

    def createLayout(self):
        self.topFrame = tk.Frame(self.root)
        self.topFrame.pack(side="top", fill="x",pady=10)

        self.bottomFrame = tk.Frame(self.root)
        self.bottomFrame.pack(side="bottom", fill="both", expand=True)

        self.leftFrame = tk.Frame(self.bottomFrame)
        self.leftFrame.pack(side="left", fill="both", expand=True)

        self.rightFrame = tk.Frame(self.bottomFrame)
        self.rightFrame.pack(side="right", fill="both", expand=True)

    def createButtons(self):
        self.uploadButton = tk.Button(self.topFrame, text="Upload Graph File",width=20, height=2,  font=("Segoe UI", 14, "bold"),bg="#2d7ff9", fg="white", command=self.uploadMatrix)
        self.uploadButton.pack(pady=10)

        self.showInfoButton = tk.Button(self.topFrame, text="Show Graph Info",width=20, height=2,  font=("Segoe UI", 14, "bold"),bg="#2d7ff9", fg="white", command=self.showGraphInfo)
        self.showInfoButton.pack(pady=10)

    def createTextBox(self):
        self.txtInfo = scrolledtext.ScrolledText(
            self.root, width=80, height=20, font=("Segoe UI", 12)
            )
        self.txtInfo.pack(pady=10)
    
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
            self.showText(self.graph.graphInfo())

    def showText(self, text: str):
        self.txtInfo.config(state="normal")
        self.txtInfo.delete(1.0, tk.END)
        self.txtInfo.insert(tk.END, text)
        self.txtInfo.config(state="disabled")

root = tk.Tk()
app = App(root)
root.mainloop()
import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def buildNetworkxGraph(graph):
    G = nx.DiGraph() if graph.isDirected else nx.Graph()
    for node in graph.nodes:
        G.add_node(node.name)
    for edge in graph.edges:
        G.add_edge(edge.source.name, edge.target.name, weight=edge.weight)
    return G

def drawGraph(graph, frame, highlightPath=None):
    G = buildNetworkxGraph(graph)

    fig = Figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    pos = nx.spring_layout(G, seed=42)   # seed fija = mismo layout cada vez, más fácil de comparar

    highlightEdges = set()
    if highlightPath:
        for i in range(len(highlightPath) - 1):
            highlightEdges.add((highlightPath[i].name, highlightPath[i+1].name))

    normalEdges = [e for e in G.edges() if e not in highlightEdges]

    # 1. dibuja los nodos
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color="#2d7ff9", node_size=800)
    nx.draw_networkx_labels(G, pos, ax=ax, font_color="white")

    # 2. dibuja primero las aristas normales, en gris (no negro, para que el rojo resalte más)
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=normalEdges, edge_color="#cccccc",
                            arrows=graph.isDirected, width=1.5)

    # 3. dibuja ENCIMA las aristas del camino, en rojo y más gruesas
    if highlightEdges:
        nx.draw_networkx_edges(G, pos, ax=ax, edgelist=list(highlightEdges),
                                edge_color="red", arrows=graph.isDirected, width=3)

    edgeLabels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edgeLabels, ax=ax, font_size=9)

    for widget in frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
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

def drawGraph(graph, frame):
    G = buildNetworkxGraph(graph)

    fig = Figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    pos = nx.spring_layout(G)
    nx.draw(G,pos,ax=ax,with_labels=True, node_color="#2d7ff9",font_color="black", node_size=800, arrows=graph.isDirected)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_size=10)

    for widget in frame.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
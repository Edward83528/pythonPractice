import graphviz as gv
import functools

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')

g3 = graph()
g4 = digraph()


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph


import itertools

l1 = ['Apple', 'Google', 'Facebook', 'Amazon']
g3 = add_nodes(g3, l1)
edges1 = [e for e in itertools.combinations(l1, 2)]
print edges1
g3 = add_edges(g3, edges1)
g3.render('graph\\demo62')

n1 = ('A', {'label': 'HTC'})
n2 = ('B', {'label': 'ACER'})
n3 = ('C', {'label': 'ASUS'})
n4 = ('D', {'label': 'GIGA'})
nodes2 = [n1, n2, n3, n4]
g4 = add_nodes(g4, nodes2)
e1 = (('A', 'B'), {'label': "VR Related"})
e2 = (('A', 'C'), {'label': 'mobile marketshare'})
e3 = (('B', 'D'), {'label': "ODM"})
e4 = (('C', 'D'), {'label': 'competitor'})
edges = [e1, e2, e3, e4]
g4 = add_edges(g4, edges)
g4.render('graph\\demo62_2')
styles = {'graph': {
    'label': 'taiwan brand',
    'fontsize': '24',
    'fontcolor': '#990000',
    'bgcolor': '#C0FFEE',
    'rankdir': 'TB',
    'fillcolor': '#FFC0EE'},
    'node': {
        'fontname': 'Courier',
        'fontsize': '24',
        'fontcolor': '#000000',
        'shape': 'box',
        'style': 'filled',
        'fillcolor': '#EEC0FF',
        'bgcolor': '#EEC0FF',
        'color': '#FFC0EE'
    },
    'edge':{
        'style':'dotted',
        'color':'#AAAAAA',
        'arrowhead':'open',
        'fontsize':'24',
        'fonrname':'Consolas',
        'fontcolor':'#66FF66'
    }
}


def apply_styles(graph, styles):
    graph.graph_attr.update(('graph' in styles and styles['graph']) or {})
    graph.node_attr.update(('node' in styles and styles['node']) or {})
    graph.edge_attr.update(('edge' in styles and styles['edge']) or {})
    return graph


g5 = graph()
g5 = apply_styles(g4, styles)
g5.render('graph\\demo62_3')

import graphviz as gv

#g1 = gv.Graph(format='svg')
g1 = gv.Digraph(format='svg')
g1.node('A')
g1.node('B')
g1.node('C')
g1.node('D')
g1.edge('A', 'A')
g1.edge('A', 'B')
g1.edge('B', 'A')
g1.edge('B', 'C')
g1.edge('A', 'D')
g1.edge('C', 'C')
g1.edge('C', 'D')

g1.render('graph\\demo61')

"""
@file
@brief Helpers around language grammar.
This module requires `antlr4 <https://pypi.python.org/pypi/antlr4-python3-runtime/>`_.
"""
from antlr4 import ParseTreeListener


class TreeGraphListener(ParseTreeListener):

    """
    This class is an attempt to run through the tree
    and to convert into a graph.

    .. exref::
        :title: Draw a grammar graph for a small code

        ::

            from pyensae.languages import get_parser_lexer, parse_code, get_tree_graph
            from pyensae.graph_helper import run_dot

            code = '''
            namespace hello
            {
                public static class world
                {
                    public static double function(double x, doubly y)
                    {
                        return x+y ;
                    }
                }
            }
            '''

            clparser, cllexer = get_parser_lexer("C#")
            parser = parse_code(code, clparser, cllexer)
            tree = parser.compilation_unit()
            st = get_tree_graph(tree, parser)
            dot = st.to_dot()

            with open(name, "w") as f:
                f.write(dot)
            img = os.path.join(temp, "graph.png")
            run_dot(name, img)
    """

    def __init__(self, parser, verbose=False, fLOG=None):
        """
        constructor

        @param      parser      parser used to parse the code
        @param      verbose     display information along the path
        @param      fLOG        logging function
        """
        ParseTreeListener.__init__(self)
        self.parser = parser
        self.vertices = {}
        self.edges = {}
        self.verbose = verbose
        self.fLOG = fLOG

    @property
    def Vertices(self):
        """
        return vertices
        """
        return self.vertices

    @property
    def Edges(self):
        """
        return edges
        """
        return self.edges

    def _get_key_node(self, node):
        line, col = node.symbol.line, node.symbol.column
        return line, col, "#END#"

    def _get_key_context(self, ctx):
        line, col = ctx.start.line, ctx.start.column
        class_name = ctx.__class__.__name__
        if class_name.endswith("Context"):
            class_name = class_name[0].lower() + class_name[1:-7]
        return line, col, class_name

    def visitTerminal(self, node):
        """
        event
        """
        key = self._get_key_node(node)
        val = (node.getText(), node, node.parentCtx)
        self.vertices[key] = val
        kc = self._get_key_context(node.parentCtx)
        self.edges[kc, key] = 1

    def visitErrorNode(self, node):
        """
        event
        """
        key = self._get_key_node(node)
        val = ("#ERROR#", node, node.parentCtx)
        self.vertices[key] = val
        kc = self._get_key_context(node.parentCtx)
        self.edges[kc, key] = 1

    def enterEveryRule(self, ctx):
        """
        event
        """
        key = self._get_key_context(ctx)
        self.vertices[key] = (key[-1], ctx, ctx.parentCtx)
        if ctx.parentCtx is not None:
            kc = self._get_key_context(ctx.parentCtx)
            self.edges[kc, key] = 1

        if self.verbose:
            self.fLOG("+", type(ctx), ctx)
            self.fLOG("+", ctx.__dict__.keys())
            self.fLOG("  +", type(ctx.start), ctx.start)
            self.fLOG("  +", ctx.start.__dict__.keys())
            text = ctx.getText()
            print("  text:", text)
            if "node" in ctx.__dict__:
                self.fLOG("  +", type(ctx.node), ctx.node)
                self.fLOG("  +", ctx.node.__dict__.keys())

    def exitEveryRule(self, ctx):
        """
        event
        """
        if self.verbose:
            self.fLOG("-", type(ctx), ctx)

    def to_networkx(self):
        """
        convert the graph into networkx

        @return     `networkx Graph <https://networkx.github.io/documentation/latest/tutorial/tutorial.html?highlight=graph>`_
        """
        import networkx  # pylint: disable=C0415
        verti = self.Vertices
        edges = self.Edges

        G = networkx.Graph()
        for v in verti:
            G.add_node(v)
        for k in edges:
            G.add_edge(k[0], k[1])
        return G

    def draw(self, ax=None):
        """
        draw the graph with networkx on matplotlib

        @param      matplotlib axis
        """
        if ax is None:
            import matplotlib.pyplot as plt  # pylint: disable=C0415
            fig, ax = plt.subplots()

        G = self.to_networkx()

        import networkx  # pylint: disable=C0415
        pos = networkx.spring_layout(G)  # positions for all nodes
        verti = self.Vertices
        labels = {p: verti[p][0] for p in pos}

        networkx.draw_networkx_nodes(G, pos, ax=ax)
        networkx.draw_networkx_edges(G, pos, ax=ax)
        networkx.draw_networkx_labels(G, pos, labels, font_size=16)

    def to_dot(self):
        """
        export the graph to DOT format

        @return         string
        """
        verti = self.Vertices
        edges = self.Edges

        ids = {}
        for k in verti:
            ids[k] = len(ids)

        rows = ["digraph {"]
        for k, v in verti.items():
            rows.append('%d [label="%s"];' % (
                ids[k], v[0].replace("\\", "\\\\").replace('"', '\\"')))
        for k in edges:
            a, b = ids[k[0]], ids[k[1]]
            rows.append("%d -> %d ;" % (a, b))
        rows.append("}")
        return "\n".join(rows)

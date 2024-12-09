import sys
from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
#from graphviz import Digraph
from pythonLexer import pythonLexer
from pythonParser import pythonParser
from anytree import Node, RenderTree

def visualize_parse_tree_console(tree, parser):
    def build_tree(node, parent=None):
        node_text = Trees.getNodeText(node, parser.ruleNames)
        tree_node = Node(node_text, parent=parent)
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            build_tree(child, tree_node)
        return tree_node
    root = build_tree(tree)
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")

#this is commented out so that main.py is not reliant on graphviz.
"""
def visualize_parse_tree_graph(tree, parser):
    def build_graph(node, graph, parent_id=None, node_id=0):
        if isinstance(node, TerminalNodeImpl):
            node_text = str(node.getText())
        else:
            node_text = Trees.getNodeText(node, parser.ruleNames)
        if not node_text.strip():
            node_text = "NL"
        current_id = str(node_id)
        graph.node(current_id, node_text)
        if parent_id is not None:
            graph.edge(parent_id, current_id)
        child_id = node_id + 1
        for i in range(node.getChildCount()):
            child_id = build_graph(node.getChild(i), graph, current_id, child_id)
        return child_id
    graph = Digraph(format="png")
    build_graph(tree, graph)
    graph.render("parse_tree", format="png", cleanup=True)
    print("Parse tree saved as 'parse_tree.png'.")
"""

def main():
    input_file = 'project_deliverable_3.py'
    input_stream = FileStream(input_file)
    lexer = pythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = pythonParser(token_stream)
    print("Token Stream:")
    token_stream.fill()
    for count, token in enumerate(token_stream.tokens):
        if token.type == pythonLexer.NL:
            print(f"{count}:{parser.symbolicNames[token.type]}: '\\n'")
        else:
            print(f"{count}:{parser.symbolicNames[token.type]}: '{token.text}'")
    print("\nParse Tree:")
    tree = parser.program()
    print(Trees.toStringTree(tree, None, parser))
    mode = input("Enter 'test' to print the parse tree or 'png' to generate a PNG: ").strip().lower()
    if mode == 'test':
        print("\nTesting parse tree visualization in the console:")
        visualize_parse_tree_console(tree, parser)
    elif mode == 'png':
        #visualize_parse_tree_graph(tree, parser)
        pass



main()
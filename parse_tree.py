from graphviz import Digraph


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def build_parse_tree(history, start_symbol="S"):

    root = Node(start_symbol)
    expandable = [root]

    for symbol, production, position in history:

        current_node = None

        for i, node in enumerate(expandable):
            if node.value == symbol:
                current_node = node
                expandable.pop(i)
                break

        if current_node is None:
            continue

        if production == "":
            current_node.children.append(Node("ε"))
            continue

        for char in production:
            child = Node(char)
            current_node.children.append(child)

            if char.isupper():
                expandable.append(child)

    return root


def draw_parse_tree(root, filename="parse_tree"):

    dot = Digraph()
    counter = [0]

    def add(node, parent=None):

        node_id = str(counter[0])
        counter[0] += 1

        dot.node(node_id, node.value)

        if parent is not None:
            dot.edge(parent, node_id)

        for c in node.children:
            add(c, node_id)

    add(root)

    dot.render(filename, format="png", cleanup=True)

    print(f"\n🌳 Parse tree saved as {filename}.png")
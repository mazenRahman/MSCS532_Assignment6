class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    # Add a child to the current node
    def add_child(self, child_node):
        self.children.append(child_node)

    # Recursive traversal of the tree
    def traverse(self):
        print(self.value)
        for child in self.children:
            child.traverse()

class RootedTree:
    def __init__(self):
        self.root = None

    # Example Usage
    def example(self):
        print("Rooted Tree Example:")
        self.root = TreeNode("Root")
        child1 = TreeNode("Child 1")
        child2 = TreeNode("Child 2")
        grandchild1 = TreeNode("Grandchild 1")
        grandchild2 = TreeNode("Grandchild 2")

        # Build the tree
        self.root.add_child(child1)
        self.root.add_child(child2)
        child1.add_child(grandchild1)
        child2.add_child(grandchild2)

        print("Tree Traversal:")
        self.root.traverse()
tree = RootedTree()
tree.example()

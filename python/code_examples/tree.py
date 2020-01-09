class node:
    def __init__(self, data):
        self._data = data
        self._children = []

    def __repr__(self):
        return self._data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def children(self):
        return self._children

    def add(self, node):
        self._children.append(node)

    def remove(self, node):
        self._children.remove(node)

class tree:

    def __init__(self, root):
        self._root = root

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, value):
        self._root = value

    def traverse_BF(self, callback):
        traversal = [self._root]

        while len(traversal) > 0:
            item = traversal[0]
            traversal.extend(item.children)
            callback(item.data)
            traversal.pop(0)
        
    def traverse_DF(self):
        return None

#creating tree nodes        
node1 = node(1)
node2 = node(2)
node3 = node(3)
node21 = node(21)
node22 = node(22)
node23 = node(23)
node2.add(node21)
node2.add(node22)
node2.add(node23)
node1.add(node2)
node1.add(node3)
tree = tree(node1)

#traversal
tree.traverse_BF(lambda x: print(x))
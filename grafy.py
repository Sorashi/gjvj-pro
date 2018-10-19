class Node:
    def __init__(self, value = 0):
        self.connections = []
        self.value = value
    def add_edge(self, other):
        self.connections.append(other)
        other.connections.append(self)

if __name__ == "__main__":
    root = Node(123)
    another = Node(321)
    root.add_edge(another)
    assert root.connections[0] == another
    assert another.connections[0] == root
    assert root.connections[0].value == another.value

from node import TreeNode

root = TreeNode("R")
vstup = [
    ['R', 'A'],
    ['R', 'B'],
    ['R', 'C'],
    ['A', 'D'],
    ['A', 'E'],
    ['A', 'F'],
    ['B', 'G'],
    ['B', 'H'],
    ['B', 'I'],
    ['B', 'J']
    ]
slovnik = {}
for i in vstup:
    if i[0] == 'R':
        
        root.add_child(i[1])

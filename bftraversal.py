class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def bft(node):
  thislevel = [node]
  while thislevel:
    nextlevel = list()
    for n in thislevel:
      print(n.value)
      if n.left: 
          nextlevel.append(n.left)
      if n.right:
          nextlevel.append(n.right)
    print
    thislevel = nextlevel

# Establish the initial root node and children
root = Node('A')
root.left = Node('B')
root.right = Node('C')

# Add the appropriate children for ‘B’ and ‘C’
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

# final level
root.left.left.left = Node('H')
root.left.left.right = Node('I')
root.left.right.left = Node('J')
root.left.right.right = Node('K')
root.right.left.left = Node('L')
root.right.left.right = Node('M')
root.right.right.left = Node('N')
root.right.right.right = Node('O')

bft(root)









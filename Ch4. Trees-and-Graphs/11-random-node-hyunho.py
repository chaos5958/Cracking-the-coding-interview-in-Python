import random

def getRandomNode(root):
    if not root:
        return None

    nodes = []
    getAllNodes(root, nodes)

    random_node = nodes[random.randint(0, len(nodes)-1)]
    return random_node

def getAllNodes(root, nodes):
    if not root:
        return

    nodes.append(root)

    getAllNodes(root.left, nodes)
    getAllNodes(root.right, nodes)

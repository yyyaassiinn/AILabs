import math

def MINIMAX(node, depth, isMaximizingPlayer):
    if node.isterminal() or depth == 0:
        return node.evaluate()
    if isMaximizingPlayer:
        bestValue = -math.inf
        for child in node.get_children():
            value = MINIMAX(child,depth-1,False)
            bestValue = max(bestValue, value)
        return bestValue
    else:
        bestValue = math.inf
        for child in node.get_children():
            value = MINIMAX(child,depth-1,True)
            bestValue = min(bestValue, value)
        return bestValue
class Node:
    def __init__ (self,value = None, children = None):
        self.value = value
        self.children = children or []
    def isterminal(self):
        return len(self.children)==0
    def get_children(self):
        return self.children
    def evaluate(self):
        return self.value

n1 = Node(3)
n2 = Node(5)
n3 = Node(2)
n4 = Node(9)
n5 = Node(children=[n1,n2])
n6 = Node(children=[n3,n4])
root = Node(children=[n5,n6])
result = MINIMAX(root,2,True)

print("best value: " ,result)
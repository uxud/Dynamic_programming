from sys import stdin

class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0

def dfs(root,a):
    if a==-1:
        for child in root.child:
            if(root.ratatosk==True):
                a=nodes.index(root)
                break
            else:
                a=dfs(child,a)
    return a

def bfs(root):
    ku=[]
    ku.append(root)
    while (len(ku)!=0):
        currentNode=ku.pop(0)
        if currentNode.ratatosk== True:
            return nodes.index(currentNode)
        for child in currentNode.child:
            ku.append(child)
    return 'nothing' 
            
        

function = stdin.readline().strip()
number_of_nodes = int(stdin.readline())
nodes = []
for i in range(number_of_nodes):
    nodes.append(Node())
start_node = nodes[int(stdin.readline())]
ratatosk_node = nodes[int(stdin.readline())]
ratatosk_node.ratatosk = True
for line in stdin:
    number = line.split()
    temp_node = nodes[int(number.pop(0))]
    for child_number in number:
        temp_node.child.append(nodes[int(child_number)])

if function == 'dfs':
    print(dfs(start_node,-1))
    
elif function == 'bfs':
    print(bfs(start_node))
elif function == 'velg':
     print(dfs(start_node))

import ast

# reading the data from the file
with open('graph.txt') as f:
    data = f.read()

# reconstructing the data as a dictionary
graph_data = ast.literal_eval(data)
print ("the graph data readed by another file is :",graph_data)
visited = [] # List for visited nodes.
queue = [] # Initialize a queue
def bfs(visited, graph, node): # function for BFS
    visited.append(node)
    queue.append(node)
    while queue: # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph_data, '5') # function calling
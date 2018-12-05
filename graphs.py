from collections import deque

class Vertex:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self):
        self.adjacency_list = []

    def add_edge(self, vertex, neighbor):
        temp = vertex
        while temp.next is not None:
            temp = temp.next

        new_vertex = Vertex(neighbor)
        temp.next = new_vertex

    def dfs(self, vertex, stack = [], visited = []):
        while vertex is not None:
            if vertex.data not in visited:
                print(vertex.data)
                stack.append(vertex)
                visited.append(vertex.data)
                vertex = [i for i in self.adjacency_list if i.data == vertex.data][0]
                vertex = vertex.next
            else:
                vertex = vertex.next
        if len(stack) == 0:
            return
        self.dfs(stack.pop(), stack, visited)

    def bfs(self, vertex, queue = deque(), visited = []):
        queue.append(vertex)
        while queue:
            vertex = queue.popleft()
            vertex = [i for i in self.adjacency_list if i.data == vertex.data][0]
            visited.append(vertex.data)
            print(vertex.data)
            while vertex is not None:
                if vertex.data not in visited:
                    visited.append(vertex.data)
                    queue.append(vertex)
                    vertex = vertex.next
                else:
                    vertex = vertex.next

def main():
    p1 = Vertex("p1")
    p2 = Vertex("p2")
    p3 = Vertex("p3")
    p4 = Vertex("p4")
    p5 = Vertex("p5")
    p6 = Vertex("p6")
    p7 = Vertex("p7")

    my_graph = Graph()
    my_graph.add_edge(p1, "p2")
    my_graph.add_edge(p1, "p3")
    my_graph.add_edge(p2, "p1")
    my_graph.add_edge(p2, "p3")
    my_graph.add_edge(p2, "p4")
    my_graph.add_edge(p2, "p5")
    my_graph.add_edge(p3, "p1")
    my_graph.add_edge(p3, "p2")
    my_graph.add_edge(p4, "p2")
    my_graph.add_edge(p4, "p6")
    my_graph.add_edge(p4, "p7")
    my_graph.add_edge(p5, "p2")
    my_graph.add_edge(p6, "p4")
    my_graph.add_edge(p7, "p4")

    my_graph.adjacency_list.append(p1)
    my_graph.adjacency_list.append(p2)
    my_graph.adjacency_list.append(p3)
    my_graph.adjacency_list.append(p4)
    my_graph.adjacency_list.append(p5)
    my_graph.adjacency_list.append(p6)
    my_graph.adjacency_list.append(p7)

    my_graph.dfs(p1)
    print("-----")
    my_graph.bfs(p1)


main()

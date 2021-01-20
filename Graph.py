class Graph:
    def __init__(self, listOfSchedule):
        self.colors = []
        self.stack = []
        self.numOfVertices = self.getTransactionNumber(listOfSchedule) + 1
        self.adjacency_Matrix = [[0 for x in range(self.numOfVertices)] for y in range(self.numOfVertices)]
        self.buildGraph(listOfSchedule)
        for vertex in range(self.numOfVertices):
            self.colors.append("white")

    @staticmethod
    def getTransactionNumber(schedule):
        size = 0
        for item in schedule:
            size = max(size, item.get_transaction())

        return size

    def init_matrix(self):
        for row in range(self.numOfVertices):
            for col in range(self.numOfVertices):
                self.adjacency_Matrix[row][col] = 0

    def buildGraph(self, listOfSchedule):
        # self.init_matrix()
        for i in range(len(listOfSchedule)):
            i_transaction = listOfSchedule[i].get_transaction()
            i_item = listOfSchedule[i].get_item()
            i_operation = listOfSchedule[i].get_operation()
            for j in range(i+1, len(listOfSchedule)):
                j_transaction = listOfSchedule[j].get_transaction()
                j_item = listOfSchedule[j].get_item()
                j_operation = listOfSchedule[j].get_operation()
                if i_transaction != j_transaction:
                    if i_item == j_item:
                        if "W" in i_operation or "W" in j_operation:
                            self.adjacency_Matrix[listOfSchedule[i].get_transaction()][
                                listOfSchedule[j].get_transaction()] = 1

    def topological_sort(self):
        for vertex in range(1, self.numOfVertices):
            if self.colors[vertex] == "white":
                if not self.visit(vertex):
                    self.stack = None

    def visit(self, vertex):
        self.colors[vertex] = "gray"
        for neighbor in range(1, self.numOfVertices):
            if self.adjacency_Matrix[vertex][neighbor] == 1:
                if self.colors[neighbor] == "gray":
                    return False
                if self.colors[neighbor] == "white":
                    self.visit(neighbor)
        self.colors[vertex] = "black"
        self.stack.append(vertex)
        return True

    def get_topological_sort(self):
        if self.stack is None:
            print("Cycle has been found!")
        else:
            while self.stack:
                print(self.stack.pop())
                if self.stack:
                    print("->")

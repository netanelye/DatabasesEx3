class Graph:
    def __init__(self, listOfSchedule):
        self.is_cycle = False
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
        for i in range(len(listOfSchedule)):
            i_transaction = listOfSchedule[i].get_transaction()
            i_item = listOfSchedule[i].get_item()
            i_operation = listOfSchedule[i].get_operation()
            for j in range(i + 1, len(listOfSchedule)):
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
                if not self.is_cycle:
                    self.visit(vertex)
                else:
                    return

    def visit(self, vertex):
        self.colors[vertex] = "gray"
        if not self.is_cycle:
            for neighbor in range(1, self.numOfVertices):
                if self.adjacency_Matrix[vertex][neighbor] == 1:
                    if self.colors[neighbor] == "gray":
                        self.is_cycle = True
                        return
                    if self.colors[neighbor] == "white":
                        self.visit(neighbor)
            self.colors[vertex] = "black"
            self.stack.append(vertex)

    def get_topological_sort(self):
        if self.is_cycle:
            print("Cycle has been found!")
        else:
            while self.stack:
                print(self.stack.pop(), end='')
                if self.stack:
                    print("->", end='')

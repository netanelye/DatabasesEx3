from Graph import Graph
from TransactionItem import TransactionItem


def createList(listOfScheduleAsString):
    listOfTransactionItems = []
    for item in listOfScheduleAsString:
        listOfTransactionItems.append(TransactionItem(item.strip().upper()))

    return listOfTransactionItems


def main():
    scheduleAsString = input("Please enter a schedule\n")
    # scheduleAsString = "r2(A);r1(B);w2(A);r2(B);r3(A);w1(B);w3(A);w2(B)"
    # scheduleAsString = "R2(A);R1(B);W2(A);R2(B);R3(A);W1(B);W3(A);W2(B)"
    # scheduleAsString = "R2(A);R1(B);W2(A);R3(A);W1(B);W3(A);R2(B);W2(B)"
    listOfSchedule = createList(scheduleAsString.split(";"))
    # print(listOfSchedule)
    graph = Graph(listOfSchedule)
    graph.topological_sort()
    graph.get_topological_sort()


if __name__ == '__main__':
    main()

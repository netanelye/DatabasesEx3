from Graph import Graph
from TransactionItem import TransactionItem


def createList(listOfScheduleAsString):
    listOfTransactionItems = []
    for item in listOfScheduleAsString:
        listOfTransactionItems.append(TransactionItem(item.strip()))

    return listOfTransactionItems


def main():
    # scheduleAsString = input("Please enter a schedule\n")
    scheduleAsString = "R2(A);R1(B);W2(A);R2(B);R3(A);W1(B);W3(A);W2(B)"
    listOfSchedule = createList(scheduleAsString.split(";"))
    # print(listOfSchedule)
    graph = Graph(listOfSchedule)
    graph.topological_sort()
    graph.get_topological_sort()


if __name__ == '__main__':
    main()

from Graph import Graph
from TransactionItem import TransactionItem


def createList(listOfScheduleAsString):
    listOfTransactionItems = []
    for item in listOfScheduleAsString:
        listOfTransactionItems.append(TransactionItem(item.strip().upper()))

    return listOfTransactionItems


def main():
    scheduleAsString = input("Please enter a schedule\n")
    listOfSchedule = createList(scheduleAsString.split(";"))
    graph = Graph(listOfSchedule)
    graph.topological_sort()
    graph.get_topological_sort()


if __name__ == '__main__':
    main()

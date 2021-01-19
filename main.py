def buildGraph(schedule):
    size = getTransactionNumber(schedule) + 1
    mat = init_matrix(size)
    for i in range(len(schedule)):
        first_operation = schedule[i][0]
        first_trans = int(schedule[i][1])
        first_item = schedule[i][2]
        j = i + 1
        for j in range(len(schedule)):
            second_trans = int(schedule[j][1])
            if first_trans != second_trans:




def init_matrix(size):
    return [[0 for x in range(size)] for y in range(size)]


def getTransactionNumber(schdule):
    size = 0
    for item in schdule:
        number = int(item[1])
        size = max(size, number)

    return size


def main(name):
    scheduleAsString = input("Please enter a schedule\n")
    listOfSchdule = scheduleAsString.split(";")
    [item.strip() for item in listOfSchdule]
    print(listOfSchdule)
    Mat = buildGraph(listOfSchdule)


if __name__ == '__main__':
    main('PyCharm')

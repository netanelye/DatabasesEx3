class TransactionItem:
    def __init__(self, objectAsStr):
        self.__operation = objectAsStr[0]
        self.__transaction = int(objectAsStr[1])
        self.__item = objectAsStr[3]
        # print("hi")

    def get_transaction(self):
        return self.__transaction

    def get_operation(self):
        return self.__operation

    def get_item(self):
        return self.__item

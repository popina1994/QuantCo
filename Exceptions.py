from typing import List


class WrongListElemType(Exception):
    def __init__(self, list: List, type_name: str):
        self.message = "All types of the element in the passed list should be " + type_name
        super().__init__(self.message)


class WrongIndexType(Exception):
    def __init__(self, index):
        self.message = "An index type should be either integer or boolean Series " + str(index)
        super().__init__(self.message)


class WrongSeriesLengths(Exception):
    def __init__(self):
        self.message = "Series should have the same lenghts "
        super().__init__(self.message)


class WrongOperationTypes(Exception):
    def __init__(self, op: str):
        self.message = "Series should have the same types and lenghts for the operation" + op
        super().__init__(self.message)


class WrongTypeNumerical(Exception):
    def __init__(self, op: str):
        self.message = "Series should be numerical for the operation " + op
        super().__init__(self.message)


class WrongTypeBool(Exception):
    def __init__(self, op: str):
        self.message = "Series should be Boolean for the operation " + op
        super().__init__(self.message)
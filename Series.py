from typing import List
from enum import Enum
from Exceptions import WrongListElemType, WrongIndexType, WrongOperationTypes, WrongTypeNumerical, WrongTypeBool

# TODO: Instead of Enum, we could use python builtin types in order to make the code more readable and accessible
# outside of this library.
class Type(Enum):
    INT = 1
    FLOAT = 2
    STRING = 3
    BOOL = 4

# Used for storing Series class. 4 classes are derived from it for the easier type handling.
# These 4 classes could have been omitted. Stronger type enforcing when typing (the programmer needs to be careful
# when they write the code)
class Series:
    typeToName = {Type.INT: "INT", Type.FLOAT: "FLOAT", Type.STRING: "STRING", Type.BOOL: "BOOL"}

    def __init__(self, typeElems: Type, name: str, elems: List):
        self.set_type(typeElems)
        self.set_name(name)
        self.set_list(elems)
        self.check_types()

    def set_name(self, name: str):
        self.name = name

    def get_name(self)-> str:
        return self.name

    def set_list(self, elems: List):
        self.elems = elems

    def get_list(self):
        return self.elems

    def get_type(self)-> str:
        return self.typeElems

    def set_type(self, typeElems: Type):
        self.typeElems = typeElems

    def get_type_name(self)-> str:
        return self.typeToName[self.typeElems]

    def get_length(self) -> int:
        return len(self.get_list())

    def __str__(self):
        outStr: str
        outStr = "Series " + self.get_type_name() + "(" + "(name: " + self.get_name() + "), (list: ["
        for elem in self.get_list():
            outStr += str(elem) + ","
        outStr = outStr.removesuffix(",")
        outStr += "]))"
        return outStr

    def __getitem__(self, index):
        if type(index) is int:
            return self.get_list()[index]
        elif type(index) is SeriesBool:
            outArr = []
            for i in range(0, self.get_length()):
                if index[i]:
                    outArr.append(self[i])
            return Series(self.get_type(), "indexed", outArr)
        else:
            raise WrongIndexType(index)

    def check_types(self):
        typeElems = self.get_type()
        for elem in self.get_list():
            elem_type = type(elem)
            #print(elem_type)
            if elem_type is str and typeElems == Type.STRING:
                continue
            if elem_type is int and typeElems == Type.INT:
                continue
            if elem_type is float and typeElems == Type.FLOAT:
                continue
            if elem_type is bool and typeElems == Type.BOOL:
                continue
            if elem is None:
                continue
            raise WrongListElemType(self.get_list(), self.get_type_name())

    @staticmethod
    def generate_series_type(name: str, type: Type, elems: List):
        if type == Type.BOOL:
            return SeriesBool(name, elems)
        elif type == Type.INT:
            return SeriesInt(name, elems)
        elif type == Type.FLOAT:
            return SeriesFloat(name, elems)
        elif type == Type.STRING:
            return SeriesString(name, elems)

    def check_equality_types(self, other, op: str):
        if isinstance(other, Series):
            if self.get_length() != other.get_length():
                raise WrongOperationTypes(op)

            if self.get_type() != other.get_type():
                raise WrongOperationTypes(op)
            return other
        elif type(other) == str:
            if self.get_type() != Type.STRING:
                raise WrongOperationTypes(op)
        elif type(other) == int:
            if self.get_type() != Type.INT:
                raise WrongOperationTypes(op)
        elif type(other) == bool:
            if self.get_type() != Type.BOOL:
                raise WrongOperationTypes(op)
        elif type(other) == float:
            if self.get_type() != Type.FLOAT:
                raise WrongOperationTypes(op)
        else:
            raise WrongOperationTypes(op)

        return Series(self.get_type(), "new", [other] * self.get_length())

    def check_numerical(self, op: str):
        if self.get_type() == Type.INT or self.get_type() == Type.FLOAT:
            return
        raise WrongTypeNumerical(op)

    def check_boolean(self, op: str):
        if self.get_type() == Type.BOOL:
            return
        raise WrongTypeBool(op)


    @staticmethod
    def eval_operation(elem1, elem2, op: str):
        if elem1 is None or elem2 is None:
            if op == "==":
                return elem1 == elem2
            if op == "!=":
                return elem1 != elem2
            return None

        if op == "+":
            return elem1 + elem2
        if op == "-":
            return elem1 - elem2
        if op == "*":
            return elem1 * elem2
        if op == "/":
            if type(elem1) == int:
                return elem1 // elem2
            else:
                return elem1 / elem2
        if op == "<":
            return elem1 < elem2
        if op == ">":
            return elem1 > elem2
        if op == "<=":
            return elem1 <= elem2
        if op == ">=":
            return elem1 >= elem2
        if op == "!=":
            return elem1 != elem2
        if op == "&":
            return elem1 & elem2
        if op == "|":
            return elem1 | elem2
        if op == "^":
            return elem1 ^ elem2
        if op == "~":
            return not elem1
        if op == "==":
            return elem1 == elem2

    # TODO: refactoring opportunites: move operation type checking from the overloaded operators to here
    # and add constraints for types based on the operation type
    # Further, generate output based on the outArr type and names based on the operations
    # TODO: Possible performance optimizations:
    # 1) vectorize the operations and parallelize the for loop
    # 2) write function wrappers in c++ and then use the optimized c++ functions using dlls
    def eval_operation_array(self, other, opStr):
        outArr = [0] * self.get_length()
        if opStr != "~":
            for i in range(0, self.get_length()):
                outArr[i] = Series.eval_operation(self[i], other[i], opStr)
        else:
            for i in range(0, self.get_length()):
                outArr[i] = Series.eval_operation(self[i], other, opStr)
        return outArr

    def __eq__(self, other):
        opStr = "=="
        other = self.check_equality_types(other, opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             Type.BOOL,
                                             outArr)
        return outSer

    def __and__(self, other):
        opStr = "&"
        other = self.check_equality_types(other, opStr)
        self.check_boolean(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             Type.BOOL,
                                             outArr)
        return outSer

    def __or__(self, other):
        opStr = "|"
        other = self.check_equality_types(other, opStr)
        self.check_boolean(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             Type.BOOL,
                                             outArr)
        return outSer

    def __xor__(self, other):
        opStr = "^"
        other = self.check_equality_types(other, opStr)
        self.check_boolean(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             Type.BOOL,
                                             outArr)
        return outSer

    def __invert__(self):
        opStr = "~"
        self.check_boolean(opStr)
        outArr = self.eval_operation_array("", opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr,
                                             Type.BOOL,
                                             outArr)
        return outSer

    def __add__(self, other):
        opStr = "+"
        other = self.check_equality_types(other, opStr)
        self.check_numerical(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             self.get_type(),
                                             outArr)
        return outSer

    def __sub__(self, other):
        opStr = "-"
        other = self.check_equality_types(other, opStr)
        self.check_numerical(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             self.get_type(),
                                             outArr)
        return outSer

    def __truediv__(self, other):
        opStr = "/"
        other = self.check_equality_types(other, opStr)
        self.check_numerical(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             self.get_type(),
                                             outArr)
        return outSer

    def __mul__(self, other):
        opStr = "*"
        other = self.check_equality_types(other, opStr)
        self.check_numerical(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             self.get_type(),
                                             outArr)
        return outSer

    def __le__(self, other):
        opStr = "<="
        other = self.check_equality_types(other, opStr)
        self.check_numerical(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             Type.BOOL,
                                             outArr)
        return outSer

    def __ge__(self, other):
        opStr = ">="
        other = self.check_equality_types(other, opStr)
        self.check_numerical(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             Type.BOOL,
                                             outArr)
        return outSer

    def __lt__(self, other):
        opStr = "<"
        other = self.check_equality_types(other, opStr)
        self.check_numerical(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             Type.BOOL,
                                             outArr)
        return outSer

    def __gt__(self, other):
        opStr = ">"
        other = self.check_equality_types(other, opStr)
        self.check_numerical(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             Type.BOOL,
                                             outArr)
        return outSer

    def __ne__(self, other):
        opStr = "!="
        other = self.check_equality_types(other, opStr)
        self.check_numerical(opStr)
        outArr = self.eval_operation_array(other, opStr)
        outSer = Series.generate_series_type(self.get_name() + opStr + other.get_name(),
                                             Type.BOOL,
                                             outArr)
        return outSer


class SeriesInt(Series):
    def __init__(self, name: str, elems: List[int]):
        super().__init__(Type.INT, name, elems)


class SeriesFloat(Series):
    def __init__(self, name: str, elems: List[float]):
        super().__init__(Type.FLOAT, name, elems)


class SeriesString(Series):
    def __init__(self, name: str, elems: List[str]):
        super().__init__(Type.STRING, name, elems)


class SeriesBool(Series):
    def __init__(self, name: str, elems: List[bool]):
        super().__init__(Type.BOOL, name, elems)
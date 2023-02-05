"""This is the summary line

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

from pippen.core.structures.frame import Frame
from pippen.core.structures.tuple import FuncTuple

class Pippen:
    def __init__(self) -> None:
        self.frame = Frame()
        self.func_queue = []

    def delete_column(self, column_name: str) -> None:
        func_tuple = FuncTuple(self.__delete_column, [column_name])
        self.func_queue.append(func_tuple)

    def __delete_column(self, column_name: str) -> None:
        self.frame.delete_column(column_name)

    def execute(self) -> None:
        for tup in self.func_queue:
            tup.getFunc()(*tup.getArgs())



    # I need a wrapper for individual functions 

    # Batch processing would involve continuously overwriting first element (row) until position is reached
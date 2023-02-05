from collections.abc import Iterable
from pippen.core.structures.frame import Frame

def load_csv_standard(reader:Iterable[str], header:list=None) -> Frame:
    # standard format has to be list of rows, which is a list of columns
    frame = Frame()

    for i, row in enumerate(reader):
        if i == 0:
            if header is None:
                header = row

            if len(header) != len(row):
                msg = 'header length does not match number of columns'
                raise ValueError(msg) 

        else:
            frame.data.append(row)

    return frame
from collections.abc import Iterable
from pippen.core.structures.frame import Frame

def load_csv_nested_dict(reader:Iterable[str], header:list=None) -> Frame:
    if not isinstance(reader, Iterable):
        raise TypeError('reader must of type iterable')

    if not isinstance(header, list):
        raise TypeError('header must of type list')
    
    frame = Frame(mode='experimental')

    for i, row in enumerate(reader):
        if i == 0:
            if header is None:
                header = row

            if len(header) != len(row):
                msg = 'header length does not match number of columns'
                raise ValueError(msg) 

        else:
            for j, column_value in enumerate(row):
                frame.data[header[j]][i] = column_value

    frame.set_header(header)

    return frame
from collections.abc import Iterable

def load_csv_standard(reader:Iterable[str]):
    header = None
    data = {}
    
    for i, row in enumerate(reader):
        if i == 0:
            if header is None:
                header = row
            self._initialize_header(len(row))
        else:
            for j, column_value in enumerate(row):
                self.data[self.header[j]][i] = column_value
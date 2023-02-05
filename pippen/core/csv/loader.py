from pippen.core.exceptions import configuration
import csv

class CsvLoader:
    def __init__(self):
        self.configs = {
            'MAX_LOAD_SIZE': 50000,
        }
        self.data = {}
        self.header = []

    def configure(self, configs:dict) -> None:
        if not isinstance(configs, dict):
            raise TypeError('configs must be of type dict')

        if 'MAX_LOAD_SIZE' in configs:
            if isinstance(configs['MAX_LOAD_SIZE'], int): 
                self.configs['MAX_LOAD_SIZE'] = configs['MAX_LOAD_SIZE']
            else:
                raise configuration.ConfigurationValueTypeException(
                    'MAX_LOAD_SIZE', 
                    'int'
                )

    def load_csv(self, csv_path:str, header:list=None) ->  dict:
        if not isinstance(csv_path, str):
            raise TypeError('csv_path must be of type str')
        
        if not isinstance(header, list) and not None:
            raise TypeError('header must be of type list')

        # if header is None, assume CSV has header
        if header is not None:
            self.header = header

        with open(csv_path) as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    if header is None:
                        self.header = row
                    self._initialize_header(len(row))
                else:
                    for j, column_value in enumerate(row):
                        self.data[self.header[j]][i] = column_value

        return self.data

    def _initialize_header(self, expected_columns_count:int) -> None:
        if not isinstance(expected_columns_count, int):
            raise TypeError('expected_columns_count must be of type int')

        self._validate_header(expected_columns_count)
        for column_name in self.header:
            self.data[column_name] = {}
            
    def _validate_header(self, expected_columns_count:int) -> None:
        if not isinstance(expected_columns_count, int):
            raise TypeError('expected_columns_count must be of type int')
            
        if len(self.header) != expected_columns_count:
            msg = 'header length does not match number of columns in file'
            raise ValueError(msg)


from typing import Union

class Frame:
    def __init__(self, mode:str="standard") -> None:
        # { column_name1: {}, column_name2: {}}
        if not isinstance(mode, str):
            raise TypeError('mode must be of type str')

        if mode == 'standard':
            self.mode = 'standard'
            self.data = []
        elif mode == 'experimental':
            self.mode = 'experimental'
            self.data = {}
        
        self.header = []

    def delete_column(self, column_name:str) -> None:
        if not isinstance(column_name, str): 
            raise TypeError('column_name must be of type str')

        if isinstance(self.data, list):
            try: 
                column_name_idx = self.header.index(column_name)
                for i, row in enumerate(self.data):
                    del row[column_name_idx]
                    self.data[i] = row

            except ValueError:
                print('Column does not exist')
            
        if isinstance(self.data, dict):
            if column_name in self.data:
                del self.data[column_name]
            else:
                print('Column does not exist')

    def set_data(self, data:Union[list, dict]) -> None:
        if isinstance(data, list) and self.mode == 'standard':
            self.data = data
        elif isinstance(data, dict) and self.mode == 'experimental':
            self.data = data
        else:
            msg = 'data must be of type list if ' + \
            'standard mode or dict if experimental mode'
            raise TypeError(msg)

    def set_header(self, header:list) -> None:
        if not isinstance(header, list):
            raise TypeError('header must be of type list')

        self.header = header

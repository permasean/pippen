class Frame:
    def __init__(self, mode:str="standard") -> None:
        # { column_name1: {}, column_name2: {}}
        if not isinstance(mode, str):
            raise TypeError('mode must be of type str')

        if mode == 'standard':
            self.data = []
        elif mode == 'experimental':
            self.data = {}
        
        self.header = []

    def delete_column(self, column_name:str) -> None:
        if not isinstance(column_name, str): 
            raise TypeError('column_name must be of type str')

        if column_name in self.data:
            del self.data[column_name]
        else:
            print('Column does not exist')

    def set_data(self, data:dict) -> None:
        if isinstance(data, dict):
            self.data = data
        else:
            raise TypeError('data must be of type dict')

    def set_header(self, header:list) -> None:
        if not isinstance(header, list):
            raise TypeError('header must be of type list')
            
        self.header = header

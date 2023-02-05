from pippen.core.csv.loader import CsvLoader
import multiprocessing as mp
import numpy as np
import sys

class Frame:
    def __init__(self) -> None:
        # { column_name1: {}, column_name2: {}}
        self.data = {}
        self.configs = {'LOAD_MAX_SIZE':50000}

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

    def load_csv(self, csv_path:str, configs:map={}) -> None:
        if not isinstance(csv_path, str): 
            raise TypeError('csv_path must be of type str')

        if not isinstance(configs, dict): 
            raise TypeError('configs must be of type dict')

        self._validate_configs(configs)
        loader = CsvLoader()
        loader.configure(configs) 
        self.set_data(loader.load_csv(csv_path)) # returns dict

    def _adjust_batch_size(self) -> None:
        mp.cpu_count()
        # Calculate optimal batch size from file
        print('PLACEHOLDER')

    def _validate_configs(self, configs:map) -> None:
        print('CONFIG VALIDATION PLACEHOLDER')
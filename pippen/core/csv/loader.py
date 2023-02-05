from pippen.core.exceptions import configuration
from pippen.core.csv import helper
import multiprocessing as mp
import csv

class CsvLoader:
    def __init__(self):
        self.configs = {
            'MAX_LOAD_SIZE': 50000,
        }

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

    def load_csv(self, csv_path:str, header:list=None, mode:str="standard") ->  dict:
        if not isinstance(csv_path, str):
            raise TypeError('csv_path must be of type str')
        
        if not isinstance(header, list) and not None:
            raise TypeError('header must be of type list')

        if not isinstance(mode, str):
            raise TypeError('mode must be of type str')

        if header is None:
            print('header not set, inferring based on first row')

        with open(csv_path) as csvfile:
            reader = csv.reader(csvfile)

            if mode == 'standard':
                frame = helper.load_csv_standard(reader, header)

        return frame

    def _adjust_batch_size(self) -> None:
        mp.cpu_count()
        # Calculate optimal batch size from file
        print('PLACEHOLDER')


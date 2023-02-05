class ConfigurationValueTypeException(Exception):
    def __init__(self, config_name:str, value_type:str) -> None:
        message = 'configuration ' + config_name + ' must have value of type ' + value_type
        super().__init__(message)
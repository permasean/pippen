class FuncTuple:
    def __init__(self, fcall:callable, args:list) -> None:
        if not isinstance(fcall, callable):
            raise TypeError('fcall must be of type callable')

        if not isinstance(args, list):
            raise TypeError('args must of type list')
        
        self._tup = tuple(fcall, args)

    def getFunc(self) -> callable:
        return self._tup[0]

    def getArgs(self) -> list:
        return self._tup[1]
    

from solution.IRainDataStorage import IRainDataStorage

class RainDataStorageList(IRainDataStorage):
    def __init__(self) -> None:
        super().__init__()
        self.ds = list()
        self.max_storage_capactiy = 10e10
    
    def add(self, object):
        self.ds.append(object)

    def get_max_capacity(self):
        return self.max_storage_capactiy

    def __iter__(self):
        return iter(self.ds)
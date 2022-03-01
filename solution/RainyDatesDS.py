class RainyDatesDS:
    def __init__(self):
        self.ds = list()

    def add(self, object):
        self.ds.append(object)
    
    def get(self, index):
        if index>=len(self.ds):
            return 0
        else:
            return self.ds[index]
    
    def __iter__(self):
        return iter(self.ds)
    
    def __len__(self):
        return len(self.ds)
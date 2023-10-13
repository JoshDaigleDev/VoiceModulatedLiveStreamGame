class DotDict:

    def __init__(self, data):
        self.data = data


    def __getattr__(self, key):
        return self.data[key]


    def __setattr__(self, key, value):
        if key == 'data':
            self.__dict__[key] = value
        else:
            self.data[key] = value

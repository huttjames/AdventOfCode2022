class Folder:
    def __init__(self, name, path, contents, size):
        self.name = name
        self.path = path
        self.contents = contents
        self.size = size

    def update_size(self, size_increase):
        new_size = self.size + size_increase
        self.size = new_size
        return new_size

class File:
    def __init__(self, name, path, size):
        self.name = name
        self.path = path
        self.size = size

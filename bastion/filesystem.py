import pickle
import os


class FileSystem:
    CONST_FILE_SYSTEM_NAME = "file_system.p"
    open_files = []

    def __init__(self):
        self.exists = self.on_disk()
        self.total_size = 0
        self.children = []
        self.root = Directory(None, "/")

    def initialize(self):
        """If the filesystem does not exist yet or we are
        overwriting the existing filesystem, run this function."""

        try:
            os.remove(self.CONST_FILE_SYSTEM_NAME)
        except IOError:
            pass

        # Overwrite old values
        self.exists = False
        self.total_size = 0
        self.children = []
        self.root = Directory(None, "/")

        # Dump the filesystem to disk.
        pickle.dump(self, open(self.CONST_FILE_SYSTEM_NAME, "wb"))

    def on_disk(self):
        if os.path.isfile(self.CONST_FILE_SYSTEM_NAME):
            return True
        else:
            return False

    def load_from_disk(self):
        pickle_load = pickle.load(open(self.CONST_FILE_SYSTEM_NAME, "rb"))
        print(dir(pickle_load))
        self.total_size = pickle_load.total_size
        self.children = pickle_load.children
        self.root = pickle_load.root
        self.exists = self.on_disk()

    def add_child(self, child):
        self.children.append(child)


class Directory:
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class File:
    def __init__(self, parent):
        self.name = None
        self.parent = parent
        self.fd = 0
        self.size = 0
        self.content = b''
        self.offset = 0

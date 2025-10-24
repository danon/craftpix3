import os
from shutil import rmtree
from tempfile import mkdtemp

def directory():
    return TemporaryDirectory()

class TemporaryDirectory:
    def __enter__(self):
        self.test_dir = mkdtemp()
        return Handle(self.test_dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        rmtree(self.test_dir)

class Handle:
    def __init__(self, dir: str):
        self.__dir = dir

    def join(self, *filenames: str) -> str:
        return os.path.join(self.__dir, *filenames).replace('\\', '/')

    def touch(self, filename: str):
        folder, _ = os.path.split(self.join(filename))
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(self.join(filename), 'w') as file:
            file.write('')

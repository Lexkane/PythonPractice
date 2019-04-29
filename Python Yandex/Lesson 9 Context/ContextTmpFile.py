import os


def main():
    pass


def generate_name():
    return "t/t/n"


class TmpFile(object):
    def __init__(self, folder):
        self.folder = folder

    def __enter__(self):
        name = generate_name()
        self.path = os.path.join(self.folder, name)
        with open(name, 'w'):
            pass
        return self.path

    def __exit__(self, exc_type, exc_value, exc_tb):
        os.remove(self.path)

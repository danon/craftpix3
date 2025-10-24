from hex.CliTerminal import CliTerminal
from hex.core.Application import Application
from test.FakeFileSystem import FakeFileSystem

def main():
    app = Application(FakeFileSystem())
    CliTerminal(app).print()

if __name__ == '__main__':
    main()

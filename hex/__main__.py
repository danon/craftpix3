import os.path

from hex.CliTerminal import CliTerminal
from hex.core.Application import Application
from hex.OsFileSystem import OsFileSystem
from hex.PygameController import PygameController
from hex.PygameEngine import PygameEngine
from hex.PygameWindow import PygameWindow

def main():
    root = os.path.dirname(os.path.dirname(__file__))
    engine = PygameEngine()
    window = PygameWindow(engine)
    app = Application(
        window,
        OsFileSystem(root),
        PygameController(engine))
    CliTerminal(app).print()

if __name__ == '__main__':
    main()

# TODO
# - game ticks and updates the element

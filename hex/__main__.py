import os.path

from hex.CliTerminal import CliTerminal
from hex.core.Application import Application
from hex.core.GameLoop import GameLoop
from hex.OsFileSystem import OsFileSystem
from hex.PygameController import PygameController
from hex.PygameEngine import PygameEngine
from hex.PygameWindow import PygameWindow
from hex.QuitAfterPolls import QuitAfterPolls

def main():
    root = os.path.dirname(os.path.dirname(__file__))
    engine = PygameEngine()
    app = Application(
        PygameWindow(engine),
        OsFileSystem(root),
        PygameController(engine))
    GameLoop(app, QuitAfterPolls(100)).start()
    CliTerminal(app).print()

if __name__ == '__main__':
    main()

# TODO
# - game ticks and updates the element

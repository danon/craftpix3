import os.path

from hex.CliTerminal import CliTerminal
from hex.core.Application import Application
from hex.OsFileSystem import OsFileSystem

def main():
    root = os.path.dirname(os.path.dirname(__file__))
    app = Application(OsFileSystem(root))
    CliTerminal(app).print()

if __name__ == '__main__':
    main()

# TODO
# - pygame accepts mouse click and directs it to the game,
#     to initiate the game element
# - game ticks and updates the element
# - pygame renders background and the frame of the element
# - quit game

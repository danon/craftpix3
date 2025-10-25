from hex.core.port import ForReadingSpriteFiles
from test.core.render_helper.FakeFileSystem import FakeFileSystem

def dummy_file_system() -> ForReadingSpriteFiles:
    return FakeFileSystem(['dummy1.png'])

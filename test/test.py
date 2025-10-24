from hex.core.Application import Application, ForControlling
from test.FakeFileSystem import FakeFileSystem

def test():
    application: ForControlling = Application(FakeFileSystem())
    assert application.resource_root() == '/root'

from pytest import raises

from hex.infra.OsFileSystem import OsFileSystem
from test.helper.directory import directory

def test_lists_files_from_directory():
    with directory() as dir:
        dir.touch('a/b/c/file.png')
        files = OsFileSystem(dir.join()).list_files('a/b')
        assert files == ['file.png']

def test_raises_for_missing_path():
    with directory() as dir:
        system = OsFileSystem(dir.join())
        with raises(Exception) as exception:
            system.list_files('missing/foo')
    assert str(exception.value) == 'Directory does not exist: missing/foo'

def test_returns_root():
    assert OsFileSystem('/root').root() == '/root'

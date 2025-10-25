from pytest import raises

from hex.infra.OsFileSystem import OsFileSystem
from test.helper.directory import directory

def test_lists_files_from_directory():
    with directory() as dir:
        dir.touch('a/b/c/file.png')
        files = OsFileSystem(dir.join()).list_files('a/b/c')
        assert files == ['file.png']

def test_raises_for_missing_path():
    with directory() as dir:
        system = OsFileSystem(dir.join())
        with raises(Exception) as exception:
            system.list_files('missing/foo')
    assert str(exception.value) == 'Directory does not exist: missing/foo'

def test_raises_for_directory_in_sprite_directory():
    with directory() as dir:
        dir.touch('sprite/directory/file.txt')
        system = OsFileSystem(dir.join())
        with raises(Exception) as exception:
            system.list_files('sprite')
    assert str(exception.value) == 'Expected a file in sprite directory, found: sprite/directory'

def test_returns_root():
    assert OsFileSystem('/root').root() == '/root'

from hex.OsFileSystem import OsFileSystem
from test.helper.directory import directory

def test_lists_files_from_directory():
    with directory() as dir:
        dir.touch('a/b/c/file.png')
        files = OsFileSystem(dir.join()).list_files('a/b')
        assert files == ['file.png']

def test_returns_root():
    assert OsFileSystem('/root').root() == '/root'

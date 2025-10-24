from hex.OsFileSystem import OsFileSystem
from test.helper.directory import directory

class Test_OsFileSystem:
    def test_lists_files_from_directory(self):
        with directory() as dir:
            dir.touch('a/b/c/file.png')
            files = OsFileSystem(dir.join()).list_files('a/b')
            assert files == ['file.png']

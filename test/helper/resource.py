import os

def resource(test_path: str):
    def res(path: str) -> str:
        return os.path.join(
            os.path.dirname(test_path),
            test_path + '.' + path)

    return res

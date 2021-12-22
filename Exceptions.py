class FileToLong(Exception):
    def __init__(self):
        print("File too long exception raised")

class MyFileNotFoundError(Exception):
    def __init__(self):
        print("File too short")

class MyException(Exception):
    def __init__(self):
        print("Error in the variable")

class NoTextError(Exception):
    def __init__(self):
        print("Text Error")
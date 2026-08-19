

class FileProcessingError(Exception):
    """Raised when there is a file read/write related issue.
          
    This exception is used to represent errors that occur during file
    read or write operations, such as missing files, invalid file
    contents, or unexpected I/O issues. Wrapping such errors in a
    custom exception allows the application to handle file-related
    failures in a consistent and meaningful way.

    """
    pass


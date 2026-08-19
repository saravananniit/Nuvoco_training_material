"""
Reads integer values from a text file and returns them as a list.

This function opens the specified file, reads it line by line, strips
whitespace, and converts each line into an integer. It handles common
file and data errors gracefully by wrapping them in a custom
FileProcessingError exception.

Error handling behavior:
- Raises FileProcessingError if the file does not exist.
- Raises FileProcessingError if any line contains non-numeric data.
- Raises FileProcessingError for any other unexpected error.

Logging behavior:
- Logs an informational message in the finally block indicating that
  a file read attempt has completed, regardless of success or failure.

Args:
    file_path (str): Path to the input file containing numeric data.
    logger (logging.Logger): Logger instance used to record status messages.

Returns:
    list[int]: A list of integers read from the file.

Raises:
    FileProcessingError: If the file is missing, contains invalid data,
    or an unexpected error occurs during processing.
"""


from exceptions import FileProcessingError

def read_numbers(file_path, logger):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [int(line.strip()) for line in file]

    except FileNotFoundError:
        raise FileProcessingError("File not found")

    except ValueError:
        raise FileProcessingError("File contains non-numeric data")

    except Exception as e:
        raise FileProcessingError(f"Unexpected error: {e}")

    finally:
        logger.info("File read attempt completed")


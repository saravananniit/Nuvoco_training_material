"""
Creates and configures a reusable application logger.

This function initializes a logger named "app_logger" with INFO level logging.
It ensures that log messages are written to the standard output (console) using
a StreamHandler and formatted with timestamp, log level, and message.

Key points:
- Uses a named logger ("app_logger") instead of the root logger to allow
  better control and separation of application logs.
- Sets the logging level to INFO so that INFO, WARNING, ERROR, and CRITICAL
  messages are captured.
- Adds a StreamHandler only if no handlers are already attached, preventing
  duplicate log outputs when the function is called multiple times.
- Applies a formatter to include:
    - asctime: timestamp of the log event
    - levelname: severity level of the log
    - message: actual log message

Returns:
    logging.Logger: A configured logger instance ready for use across the application.
"""

import logging

def setup_logger():
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

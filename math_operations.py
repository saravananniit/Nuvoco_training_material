"""
Safely performs division and logs the result.

This function divides two numbers and logs the division result if successful.
It handles the division-by-zero scenario gracefully by catching the
ZeroDivisionError and logging an appropriate error message instead of
raising an exception.

Args:
    a (int | float): Numerator value.
    b (int | float): Denominator value.
    logger (logging.Logger): Logger instance used to record messages.

Returns:
    int | float | None: The result of the division if successful,
    otherwise None when division by zero occurs.

Logging behavior:
- Logs an INFO message with the division result on success.
- Logs an ERROR message if division by zero is attempted.
"""


def safe_divide(a, b, logger):
    try:
        result = a / b
        logger.info(f"Division result: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero attempted")

def process_no(value, logger):
    try:
        number = int(value)
        logger.info(f"Processed number: {number}")
        return number
    except ValueError:
        logger.error(f"Invalid number: {value}")

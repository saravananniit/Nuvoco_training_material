# Expose selected functions at the utils package level (optional but handy).
# In modern Python (3.3+), namespace packages work without __init__.py, but most projects still use it for control and clarity.

from .math_utils import add, subtract, multiply, divide
from .string_utils import to_upper, join_with_space

__all__ = ["add", "subtract", "multiply", "divide", "to_upper", "join_with_space"]

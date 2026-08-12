from utils.math_utils import add
from utils.string_utils import to_upper
from utils.calc import add_two_numbers

# result = add(5, 3)
# print(result)

# print(to_upper("hello"))

if __name__ == "__main__":
    # Example usage of the functions
    sum_result = add(10, 20)
    print(f"Sum: {sum_result}")

    upper_text = to_upper("hello world")
    print(f"Uppercase: {upper_text}")

    print(add_two_numbers(10, 20))

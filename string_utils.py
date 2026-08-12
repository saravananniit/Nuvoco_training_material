def to_upper(text):
    return text.upper()

def join_with_space(a, b):
    return f"{a} {b}"

print("inside string_utils.py")


if __name__ == "__main__":
    # Example usage of the functions
    upper_text = to_upper("hello world")
    print(f"Uppercase: {upper_text}")

    joined_text = join_with_space("Hello", "World")
    print(f"Joined with space: {joined_text}")
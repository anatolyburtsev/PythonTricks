import re

date_like_pattern = r'^\d{4}-\d{2}-\d{2}$'
def process(date_string: str) -> str:
    assert re.match(date_like_pattern, date_string)
    return "Success"

if __name__ == "__main__":
    print(process("2022-12-12"))  # Success
    print(process("2022/12/12"))  # AssertionError
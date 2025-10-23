def get_input() -> str:
    input_str: str = input()

    return input_str

def check_input(input_str: str) -> bool:
    # Check if the input string represents a valid integer
    if input_str.isdigit():
        return True
    else:

        return False

def get_number() -> int:
    input_str: str = get_input()

    # Validate the input
    if check_input(input_str):
        return int(input_str)
    else:
        return get_number()

def iterate_process(iterations: int, function, counter: int = 0) -> None:
    # Recursive function to iterate a process
    if counter < iterations:
        function()

        counter += 1

        iterate_process(iterations, function, counter)

def get_value_strings(max_values: int) -> list[str]:
    str_values: list[str] = []

    # Get all inputs in a single line
    input_str: str = get_input()
    # Split the input string into individual values
    str_values = input_str.split()

    # Check if the values are all digits and filter accordingly
    str_values = list(filter(lambda val: val.isdigit(), str_values))

    if len(str_values) != max_values:

        return get_value_strings(max_values)

    return str_values

def get_value(number_of_values: int) -> list[int]:
    values: list[int] = []

    # Get the string of values in one line
    str_values: list[str] = get_value_strings(number_of_values)

    # Filter and convert valid inputs to integers
    values = list(filter(lambda num: num >= 0, map(int, str_values)))

    return values

def calculate_sum_of_squares(values: list[int]) -> int:
    # Calculate the sum of squares using map and lambda
    sum_squares = sum(map(lambda num: num ** 2, values))

    return sum_squares

def prepare_values() -> None:
    # Get the number of values in a line
    number_of_values: int = get_number()

    # Get the list of values
    values: list[int] = get_value(number_of_values)

    # Calculate the sum of squares
    result = calculate_sum_of_squares(values)

    print(result)


# MAIN FUNCTION
def main() -> None:
    number_of_iterations: int = get_number()

    # Gets the number of inputs from the user
    iterate_process(number_of_iterations, prepare_values)


if __name__ == "__main__":
    main()

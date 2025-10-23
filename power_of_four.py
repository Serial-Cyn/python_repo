def is_digit(data: str, index: int = 0) -> bool:
    digit: bool = True

    # Check if index is within bounds
    if index < len(data):
        # Check if current character is a digit
        if data[index] >= "0" and data[index] <= "9":
            digit = is_digit(data, index + 1) # Check next digit
        else:
            digit = False

    return digit

def get_input() -> str:
    user_input: str = input()

    return user_input.strip()

def get_number() -> int:
    user_input: str = get_input()
    number: int = 0

    # Validate input
    if is_digit(user_input):
        number = int(user_input)
    else:
        number = get_number() # Retry on invalid input

    return number

def iterate_process(num_iterations: int, func, counter: int = 0) -> None:
    # Stop when counter reaches the number of iterations
    if counter < num_iterations:
        func()

        iterate_process(num_iterations, func, counter + 1)

def get_elements(required_num: int) -> list[int]:
    user_input: str = get_input()

    # Split input into list of strings
    elements_str: list[str] = user_input.split()

    elements: list[int] = list(
        filter(
            lambda x: is_digit(x) and int(x) > 0, elements_str
        )
    )

    # Check if we have the correct number of elements
    if len(elements) != required_num:
        return get_elements(required_num)

    # Makes sure that all elements are converted to integers
    elements = list(map(int, elements))

    return elements

def is_power_of_four(num: int) -> bool:
    POWER_NUM = 4

    if num < 1:
        return False
    
    if num % POWER_NUM == 0:
        num = num // POWER_NUM

        return is_power_of_four(num)
    else:
        if num == 1:
            return True

    return False

def sum_of_list(values: list[int]) -> int:
    if len(values) == 0:
        return 0
    else:
        return values[0] + sum_of_list(values[1:])

def filter_power_of_four() -> None:
    num_of_elements: int = get_number()
    elements: list[int] = get_elements(num_of_elements)

    filtered_elements: list[int] = list(
        filter(
            lambda x: is_power_of_four(x), elements
        )
    )

    total_sum: int = sum_of_list(filtered_elements)

    print(total_sum)

def main() -> None:
    num_iterations: int = get_number()

    iterate_process(num_iterations, filter_power_of_four)

if __name__ == "__main__":
    main()
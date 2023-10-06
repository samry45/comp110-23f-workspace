"""list Utility Functions."""
__author__ = "730642818"

def all(numbers: list[int], guess: int) -> bool:
    test_idx = 0
    test_result = True
    while test_idx < len(numbers) and test_result == True:
        if numbers[test_idx] == guess:
            test_result = True
        else:
            test_result = False
        test_idx += 1
    return test_result

def max(numbers: list[int]) -> int:
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    high_num = numbers[0]
    test_idx = 0
    while test_idx < len(numbers):
        if numbers[test_idx] > high_num:
            high_num = numbers[test_idx]
        test_idx += 1
    return high_num

def is_equal(input1: list[int], input2: list[int]) -> bool:
    if input1 == input2:
        return True
    else:
        return False
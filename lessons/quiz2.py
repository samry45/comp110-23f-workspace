"""Function writing practice."""

def odd_and_even(nums: list[int]) -> list[int]:
    result: list[int] = []
    idx: int = 0
    while idx < len(nums):
        if idx % 2 == 0 and nums[idx] % 2 == 1:
            result.append(nums[idx])
        idx += 1
    return result


def value_exists(testing: dict[str, int], tested: int) -> bool:
    for keys in testing:
        if tested == testing[keys]:
            return True
    return False


def short_words(words: list[str]) -> list[str]:
    """Returns list of word that are shorter than 5 characters."""
    result: list[str] = []
    for elem in words:
        if len(elem) < 5:
            result.append(elem)
        else:
            print(f"{elem} is too long!")
    return result
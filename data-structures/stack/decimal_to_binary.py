"""
Convert Decimal to Binary
"""

from Stack import Stack


def decimal_to_binary(dec_num: int) -> int:
    """Converts a decimal integer to binary

    Args:
        decimal (int): decimal representation of the number

    Returns:
        binary (int): binary representation of the number
    """

    if dec_num == 0:
        return 0

    binary = ""

    bin_stack = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        bin_stack.push(remainder)
        dec_num = dec_num // 2

    while not bin_stack.is_empty():
        binary += str(bin_stack.pop())

    return binary


print(decimal_to_binary(83))

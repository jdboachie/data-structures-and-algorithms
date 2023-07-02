"""
Stack Data Structure
"""


class Stack():

    def __init__(self, ):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self, ):
        return self.items.pop()

    def peek(self, ):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self, ):
        return self.items == []

    def get_stack(self, ):
        return self.items


def reverse_string(input_str: str) -> str:
    """Reverses a given string

    Args:
        input_str (str): input string

    Returns:
        str: reversed string
    """
    stack = Stack()
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""

    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


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




def is_balanced_parentheses(paren_string: str) -> bool:

    def is_match(p1, p2):
        if p1 == "(" and p2 == ")":
            return True
        elif p1 == "[" and p2 == "]":
            return True
        elif p1 == "{" and p2 == "}":
            return True
        else:
            return False

    stack = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            stack.push(paren)
        else:
            if stack.is_empty():
                is_balanced = False
                break
            else:
                top = stack.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if stack.is_empty() and is_balanced:
        return True
    else:
        return False

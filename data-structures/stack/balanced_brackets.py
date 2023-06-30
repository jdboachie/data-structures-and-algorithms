"""
Determine if Brackets are Balanced
"""

from Stack import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False


def is_balanced_parentheses(paren_string):

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


print("String : (((({})))) Balanced or not?")
print(is_balanced_parentheses("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_balanced_parentheses("[][]]]"))

print("String : [][] Balanced or not?")
print(is_balanced_parentheses("[][]"))

from collections import deque

def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.
    """
    # remove spaces and convert to lowercase
    s = ''.join(s.split()).lower()

    # create a deque from the string
    d = deque(s)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Testing
print(is_palindrome("Qwe rty treWq"))  # True
print(is_palindrome("Abs ba"))  # True
print(is_palindrome("Hello World"))  # False

# We need to use Stack to check if the brackets are symmetrical

def is_symmetrical_brackets(s: str) -> bool:
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets_map = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets_map:
            if stack and stack[-1] == closing_brackets_map[char]:
                stack.pop()
            else:
                return False
    
    return True if not stack else False

def check_symmetrical_brackets(s: str) -> str:
	return "Симетрично" if is_symmetrical_brackets(s) else "Несиметрично"


print(check_symmetrical_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(check_symmetrical_brackets(")( 23 ( 2 - 3));"))  # Несиметрично
print(check_symmetrical_brackets("( 11 }"))  # Несиметрично
import re

def valid_palindrome(string):
    pattern = r'\w+'  # Regex pattern to match alphanumeric characters
    matches = re.findall(pattern, string)
    ('').join(matches)
    

# Example usage:
text = "Hello, 123 World!"
result = valid_palindrome(text)
print(result)

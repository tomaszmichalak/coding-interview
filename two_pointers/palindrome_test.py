import logging
import sys
import re

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

def is_palindrome(input: str):
    if input == '':
        return True
    input = re.sub(r'\W+', '', input)
    chars: list[str] = list(input)
    left = 0
    right = len(chars) - 1
    while left < right:
        if chars[left] != chars[right]: 
            return False
        else:
            left += 1
            right -= 1
    return True

def is_palindrome_improved(input: str):
    if input == '':
        return True
    chars: list[str] = list(input)
    left = 0
    right = len(chars) - 1
    while left < right:
        while left < right and not chars[left].isalnum():
            left += 1
        while left < right and not chars[right].isalnum():
            right -= 1
        if chars[left] != chars[right]: 
            return False
        else:
            left += 1
            right -= 1
    return True

def test_is_palindrome():
    assert is_palindrome('') == True
    assert is_palindrome('tt') == True
    assert is_palindrome('tomek') == False
    assert is_palindrome('!racecar') == True
    assert is_palindrome('racecar') == True

def test_is_paliondrome_improved():
    assert is_palindrome_improved('') == True
    assert is_palindrome('tt') == True
    assert is_palindrome_improved('tomek') == False
    assert is_palindrome_improved('!racecar') == True
    assert is_palindrome_improved('racecar') == True
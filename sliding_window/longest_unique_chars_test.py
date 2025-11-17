import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

def longest_unique_chars(s: str) -> int:
    if len(s) == 0 or len(s) == 1:
        return len(s)
    left, right = 0, 0
    unique_chars = set()

    unique_len = 0
    while right < len(s):
        log.debug(f"Unique chars: {unique_chars}, next: {s[right]}")
        if s[right] in unique_chars:
            while s[left] != s[right]:
                unique_chars.remove(s[left])
                left += 1
            left += 1 # not remove from unique chars
        unique_chars.add(s[right])
        if unique_len < right - left + 1:
            unique_len = right - left + 1
        right += 1
    return unique_len

def test_longest_unique_chars():
    assert longest_unique_chars("") == 0
    assert longest_unique_chars("a") == 1
    assert longest_unique_chars("ab") == 2
    assert longest_unique_chars("aba") == 2
    assert longest_unique_chars("abcba") == 3
    assert longest_unique_chars("abcbabcd") == 4
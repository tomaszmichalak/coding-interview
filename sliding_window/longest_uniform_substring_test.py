import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

def longest_uniform(s: str, k: int) -> int:
    freqs = {} # char -> freq
    highest_freq, unique_len = 0, 0
    left, right = 0, 0
    while right < len(s):
        freqs[s[right]] = freqs.get(s[right], 0) + 1
        highest_freq = max(highest_freq, freqs[s[right]])
        log.debug(f"Freqs: {freqs}, highest_freq: {highest_freq}, window: {s[left:right+1]}")
        if (right - left + 1) - highest_freq > k:
            freqs[s[left]] -= 1
            left += 1
        if unique_len < right - left + 1:
            unique_len = right - left + 1
        right += 1
    return unique_len

def test_longest_unique_chars():
    assert longest_uniform("", 0) == 0
    assert longest_uniform("ab", 0) == 1
    assert longest_uniform("ab", 1) == 2
    assert longest_uniform("aabccbc", 2) == 5  # "ccccc"
    assert longest_uniform("aabccbcaabaa", 1) == 5  # "aaaaa"

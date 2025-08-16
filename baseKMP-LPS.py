def build_lps(pattern: str):
    """Compute the Longest Prefix Suffix (LPS) array for KMP."""
    lps = [0] * len(pattern)
    length = 0  # length of the current longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text: str, pattern: str):
    """Return the starting indices of all occurrences of pattern in text."""
    if not pattern:
        return []

    lps = build_lps(pattern)
    i = j = 0  # i = index for text, j = index for pattern
    matches = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):  # match found
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


# ----------------
# Example usage:
# ----------------
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print("Matches at indices:", kmp_search(text, pattern))

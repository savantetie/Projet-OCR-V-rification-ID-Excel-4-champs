from rapidfuzz import fuzz

def score_pair(a: str | None, b: str | None) -> int:
    """Return a 0–100 similarity score using token sort ratio."""
    if not a or not b:
        return 0
    return int(fuzz.token_sort_ratio(str(a), str(b)))

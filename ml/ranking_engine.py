def rank_candidates(candidates):
    """Sort candidate records by score descending."""
    return sorted(candidates, key=lambda x: x.get("score", 0), reverse=True)

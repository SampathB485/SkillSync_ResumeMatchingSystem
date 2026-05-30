"""Ranking utilities placeholder."""

def rank_candidates(candidates):
    """Rank candidates by score (stub)."""
    return sorted(candidates, key=lambda x: x.get("score", 0), reverse=True)

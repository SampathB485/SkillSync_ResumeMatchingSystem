"""Ranking utilities - wrapper around ML ranking engine."""
from ml.ranking_engine import rank_candidates as ml_rank_candidates


def rank_candidates(candidates):
    """
    Rank candidates by match score (descending order).
    
    Args:
        candidates (list): List of candidate dictionaries with 'score' key
        
    Returns:
        list: Candidates sorted by score in descending order
    """
    if not candidates:
        return []
    
    return ml_rank_candidates(candidates)

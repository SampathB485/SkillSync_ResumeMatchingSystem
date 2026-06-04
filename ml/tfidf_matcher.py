from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_tfidf_match(texts):
    """
    Compute TF-IDF cosine similarity matrix for a set of texts.
    
    Args:
        texts (list): List of text documents
        
    Returns:
        numpy.ndarray: Cosine similarity matrix
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(texts)
    return cosine_similarity(tfidf_matrix)


def compute_tfidf_similarity(text1, text2):
    """
    Compute TF-IDF cosine similarity between two texts.
    
    Args:
        text1 (str): First text (e.g., resume)
        text2 (str): Second text (e.g., job description)
        
    Returns:
        float: Similarity score between 0 and 1
    """
    if not text1 or not text2:
        return 0.0
    
    try:
        # Vectorize both texts
        vectorizer = TfidfVectorizer(stop_words="english", min_df=1)
        texts = [text1, text2]
        tfidf_matrix = vectorizer.fit_transform(texts)
        
        # Compute similarity between the two vectors
        similarity_matrix = cosine_similarity(tfidf_matrix)
        
        # Return the similarity between first and second document
        return float(similarity_matrix[0][1])
    except Exception as e:
        print(f"Error computing TF-IDF similarity: {str(e)}")
        return 0.0

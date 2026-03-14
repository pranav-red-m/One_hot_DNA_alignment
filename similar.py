"""
similar.py contains 2 main functions. Cosine similarity and SVD fingerprint. THink aobut it like this matching.py will 
work on sequential alignment, while i will work on similarity which does not take into account this sequential element.

Basically i will do similarity wrt structure rather than sequence.
"""

from encoding import encode
import numpy as np


def cosine_similarity(seq1:str,seq2:str) -> float:
    if not isinstance(seq1,str) or not isinstance(seq2,str):
        raise TypeError("Input sequence must be a string.")
    
    m1 = encode(seq1).sum(axis=0) #[#A,#C,#G,#T] for mat1
    m2 = encode(seq2).sum(axis=0)

    norm = np.linalg.norm(m1) * np.linalg.norm(m2) 
    if 0 == norm:
        return 0.0
    
    return float(np.dot(m1,m2)/norm)

#Take top 2 by default, user can change if he/she wants to.
def svd_fingerprint(seq:str,k=2):
    if not isinstance(seq,str):
        raise TypeError("Input sequence must be a string.")
    
    if not isinstance(k,int) or k <= 0:
        raise ValueError("'k' must be a positive integer")
    
    m=encode(seq)

    _,s,_ = np.linalg.svd(m,full_matrices=False) #diable full matrices to save memory on runtime
    return s[:k]

def svd_distance(seq1:str,seq2:str) -> float:
    m1 = svd_fingerprint(seq1)
    m2 = svd_fingerprint(seq2)

    return float(np.linalg.norm(m1-m2))

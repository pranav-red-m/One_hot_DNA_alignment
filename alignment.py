import numpy as np #for vectors and dot product 
from encoding import encode #converts the sequence into an array 

def align(seq1,seq2): 
    mat1 = encode(seq1)
    mat2 = encode(seq2)
    
    best_score = -1
    best_shift = 0
    scores = [] #an array of all the scores for each shift
    
    for shift in range(-len(seq2),len(seq1)): #shift is how much we shift the second sequence to the right, negative means shift to the left
        score = 0
        for i in range(len(mat1)):
            j = i-shift #the index of the second sequence we are comparing to
            
            if 0<=j and j<len(mat2): #if the index is valid
                score += np.dot(mat1[i],mat2[j]) #1 if matching 
                
        scores.append(score)
        
        if score > best_score:
            best_score = score
            best_shift = shift
            
    return int(best_score), int(best_shift), [int(s) for s in scores] # this is because numpy returns numpy.int64 

def format_alignment(seq1, seq2, shift):
    if shift >= 0:
        aligned_seq1 = seq1
        aligned_seq2 = " " * shift + seq2 
    else:
        aligned_seq1 = " " * (-shift) + seq1
        aligned_seq2 = seq2

    return aligned_seq1, aligned_seq2
#couldn't stand how it looked without this 

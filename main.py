import numpy as np
import matplotlib.pyplot as plt
encoding = {
    "A":[1,0,0,0],
    "C":[0,1,0,0],
    "G":[0,0,1,0],
    "T":[0,0,0,1]
} #encoding all the genome

def encode(seq): #turn sequence of genomes to array of basis vectors
    return np.array([encoding[x] for x in seq])

def similarity(a,b): #sumof all points in dot product
    return np.sum(a*b)

#currently jsut do +1 for match ignore gaps and mismatches
def check_similarity(seq1,seq2):
    scores = []
    for shift in range(-len(seq2),len(seq1)):
        score = 0
        for i in range(len(seq1)):
            j = i-shift
            if 0<=j and j<len(seq2):
                score += np.dot(seq1[i],seq2[j])
        scores.append(score)
    return scores

#Test example
seq1 = "ACGTAC"
seq2 = "CGTACA"
encoded_seq1 = encode(seq1)
encoded_seq2 = encode(seq2)
scores = check_similarity(encoded_seq1,encoded_seq2)
print(scores)

plt.plot(scores)
plt.title("Bananas")
plt.show()
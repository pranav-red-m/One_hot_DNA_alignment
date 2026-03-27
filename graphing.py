import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from alignment import align



def plot_alignment(seq1, seq2):
    best_score, best_shift, scores = align(seq1, seq2)

    shifts = list(range(-len(seq2), len(seq1)))

    plt.plot(shifts, scores, marker='o')
    plt.title("Alignment Score vs Shift")
    plt.xlabel("Shift")
    plt.ylabel("Score")
    plt.grid()

    
    plt.axvline(x=best_shift, linestyle='--')
    
    plt.show()



from encoding import encode

def match_count(seq1, seq2):
    mat1 = encode(seq1)
    mat2 = encode(seq2)

    minlen = min(len(seq1), len(seq2))
    return int(np.trace(mat1[:minlen].T @ mat2[:minlen]))



def build_heatmap(sequences):
    n = len(sequences)
    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            matrix[i][j] = match_count(sequences[i], sequences[j])

    return matrix



def plot_heatmap(sequences):
    matrix = build_heatmap(sequences)

    sns.heatmap(matrix, annot=True, xticklabels=sequences, yticklabels=sequences)
    plt.title("DNA Sequence Similarity Heatmap")

    plt.show()
from similar import cosine_similarity, svd_fingerprint, svd_distance

from alignment import align, format_alignment

# dummy input to test the alignment function 
seq1 = "ACGTAC"
seq2 = "CGT"

best_score, best_shift, scores = align(seq1, seq2)

a1, a2 = format_alignment(seq1, seq2, best_shift)

print("Best Alignment:\n")
print(a1)
print(a2)

print("\nBest Score:", best_score)
print("Best Shift:", best_shift)

print("\n")

def run_tests():
    print("DNA Similarity Tests\n")

    test_cases = [
        ("ACGTACGT", "ACGTACGT"),   # identical
        ("ACGTACGT", "TTTTTTTT"),   # very different
        ("ACGTACGT", "TGCAACGT"),   # similar composition
        ("ACGTACGTACGT", "ACGT"),       # mostly similar
        ("ACGT", "TGCA")            # reversed order
    ]

    for seq1, seq2 in test_cases:
        print("===================================")
        print(f"Sequence 1: {seq1}")
        print(f"Sequence 2: {seq2}")

        cos = cosine_similarity(seq1, seq2)
        svd1 = svd_fingerprint(seq1)
        svd2 = svd_fingerprint(seq2)
        dist = svd_distance(seq1, seq2)

        print(f"Cosine Similarity : {cos:.4f}")
        print(f"SVD Fingerprint 1 : {svd1}")
        print(f"SVD Fingerprint 2 : {svd2}")
        print(f"SVD Distance      : {dist:.4f}")
        print()

if __name__ == "__main__":
    run_tests()
    

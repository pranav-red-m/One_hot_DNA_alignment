import numpy as np

encoding = {
    "A": np.array([1,0,0,0]),
    "C": np.array([0,1,0,0]),
    "G": np.array([0,0,1,0]),
    "T": np.array([0,0,0,1])
}

VALID_BASES = set(encoding.keys())

reverse = {tuple(v): k for k, v in encoding.items()}

def encode(seq):
    if not isinstance(seq, str):
        raise TypeError("Input sequence must be a string.")

    seq = seq.upper()

    if len(seq) == 0:
        raise ValueError("DNA sequence cannot be empty")

    for b in seq:
        if b not in VALID_BASES:
            raise ValueError(f"Invalid DNA base: {b}. Only A, C, G, T allowed.")

    return np.vstack([encoding[b] for b in seq])


def decode(arr):
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a NumPy array.")

    if arr.ndim != 2 or arr.shape[1] != 4:
        raise ValueError("Encoded array must have 4 columns.")

    seq = ""

    for row in arr:
        key = tuple(row)

        if key not in reverse:
            raise ValueError(f"Invalid encoded vector: {row}")

        seq += reverse[key]

    return seq

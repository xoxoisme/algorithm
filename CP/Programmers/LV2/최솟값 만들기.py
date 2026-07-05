def solution(A,B):
    A, B = sorted(A), sorted(B, reverse=True)
    return sum([A[i]*B[i] for i in range(len(A))])
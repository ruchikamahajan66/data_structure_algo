##Rope Cutting problem
# Given a rod of length N meters, and the rod can be cut in only 3 sizes
# A,B and C. The task is to maximizes the number of cuts in rod. If it is impossible to make cut then print -1

def solution(N, A, B, C):
    cut = 0
    if N == A or N == B or N == C:
        return 1 + cut
    if N < A or N < B or N < C:
        return -1

    A_call = solution(N - A, A, B, C)
    B_call = solution(N - B, A, B, C)
    C_call = solution(N - C, A, B, C)
    return max(A_call, B_call, C_call)


if __name__ == '__main__':
    N = 17
    A = 10
    B = 11
    C = 3
    print("mac cut", solution(N, A, B, C))

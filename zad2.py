from numpy import inf
from math import inf



def maximize_score(scores: list[int], C: int) -> tuple[int, list[int]]:
   
   
    n = len(scores)

    dp = [[-inf] * n for _ in range(C + 1)]
    parent = [[-1] * n for _ in range(C + 1)]
    dp[0][0] = scores[0]
    for c in range(1, C + 1):
        for i in range(n):
            for j in [i - 3, i - 2, i + 1]:
                if 0 <= j < n and dp[c-1][j] != -inf:
                    candidate = dp[c-1][j] + scores[i]
                    if candidate > dp[c][i]:
                        dp[c][i] = candidate
                        parent[c][i] = j
    best_score = max(dp[C])
    
    
    
    if best_score == -inf:
        return None, None
    
    
    current = dp[C].index(best_score)
    path = [current]
    for c in range(C, 0, -1):
        current = parent[c][current]
        path.append(current)
    path.reverse()
    return best_score, path



# TESTY

def test_basic():
    scores = [0, 3, -2, 5, 10, 4]
    C = 3
    best, path = maximize_score(scores, C)
    assert best == 19
    assert path == [0, 3, 5, 4]


def main():
    test_basic()
    print("Test zaliczony")


if __name__ == "__main__":
    main()

from numpy import inf
from math import inf


def maximize_score(scores: list[int], C: int) -> tuple[int, list[int]]:
    """W tym miejscu należy uzupełnić swoje rozwiązanie"""       
                   
    def top3(row):
        best = (-inf, -1)
        second = (-inf, -1)
        third = (-inf, -1)
        for idx, val in enumerate(row):
            if val > best[0]:   
                third = second
                second = best
                best = (val, idx)
            elif val > second[0]:
                third = second
                second = (val, idx)
            elif val > third[0]:
                third = (val, idx)
    
        return best, second, third
    
    def get_best_for(top, i):
        for val, idx in top:
            if idx != i and idx != i-1:
                return val
        return -inf

    
    n = len(scores)
    dp = [[-inf]*n for _ in range(C+1)]
    dp[0][0] = 0  

    for c in range(1, C+1):
            top = top3(dp[c-1])
            for i in range(n):
                best = get_best_for(top, i)
                if best != -inf:
                    dp[c][i] = scores[i] + best
    best = max(dp[C])
    if best == -inf:
        return None, None
    for c in range(C+1):
        print(f"ruch {c}: {dp[c]}")
    return best, []

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

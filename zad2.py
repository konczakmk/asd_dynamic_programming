from numpy import inf
from math import inf

"""
Idea

Algorytm, przygotowywuje macierz dp (l. wierszy = l. ruchów + 1, l. kolumn = dłg. tablicy scores), która będzie pamiętać wszystkie (najlepsze) możliwe sumy punktów otrzymane poprzez przejście,
na odpowiadające pole tabeli scores w danym ruchu. Jeśli przejście do danego pola jest niemożliwe w odpowiedniej komórce przechowywane jest -inf. 
Po przeliczeniu wszytkich sum wybierana jest największa (lub jdena z gdy jest ich kilka o tej samej wartości).

W celu odnaleznienia ścieżki algorytm korzysta z przechowywanych informacji o największej sumie i sumach w poszczególnych ruchach. Iterując wstecz po wierszach macierzy dp,
kieruje się dozwolonymi przejściami i odtwarza jedną z możliwych ścieżek, zapisując indeksy kolumn z macierzy dp, odpowiadających tym z macierzy scores.
"""


def maximize_score(scores: list[int], C: int) -> tuple[int, list[int]]:
    n = len(scores)

   if n <=0 or C <=0:
      return None, None
   
    dp = [[-inf] * n for _ in range(C + 1)]
    dp[0][0] = scores[0]
    for c in range(1, C + 1):
        for i in range(n):
            for j in [i - 3, i - 2, i + 1]:
                if 0 <= j < n and dp[c-1][j] != -inf:
                    candidate = dp[c-1][j] + scores[i]
                    if candidate > dp[c][i]:
                        dp[c][i] = candidate
    best_score = max(dp[C])
    
    
    if best_score == -inf:
        return None, None

    final_idx = dp[C].index(best_score)
    curr_idx = final_idx

    path = [final_idx]

    # Korzystajac z wcześniej utworzonej macierzy dp, wartości najlepszego wyniku oraz znanej pozycji ostatnio dodanej liczby z tablicy score, odtwarzam ścieżkę
    # Dla każdego możliwego przejścia (do czasu znaleznienia pierwszego poprawnego) sprawdzam czy dane przejście z 'prev_idx' do 'curr_idx' mogło dać obecną sumę (dp[c][curr_idx])
    # Na koniec dwracam ścieżkę
    for c in range(C, 0, -1):
       for j in [3, 2, -1]:
          prev_idx = curr_idx - j
          if 0 <= prev_idx < n and dp[c - 1][prev_idx] != -inf:
             if dp[c - 1][prev_idx] + scores[curr_idx] == dp[c][curr_idx]:
                path.append(prev_idx)
                curr_idx = prev_idx
                break
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

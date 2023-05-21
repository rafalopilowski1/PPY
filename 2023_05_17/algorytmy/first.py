import math
import sys
from typing import List


def erat(n: int) -> List[int]:
    """
    Displays first numbers found by Erastoteles algorithm

    Parameters:
    -----------
    n : int
        Max range to find first numbers

    Returns:
    --------
    list : List[int]
        A list od integers representing first numbers
    """
    imax = int(math.sqrt(n) + 1)
    primes = [True] * (n + 1)
    for i in range(2, imax + 1):
        if primes[1]:
            for j in range(i + 1, n + 1, i):
                primes[j] = False
    result = []
    for i in range(2, n + 1):
        if primes[i]:
            result.append(i)
    return result


def main():
    print(sys.argv)
    print(erat(int(sys.argv[1])))


if __name__ == "__main__":
    main()

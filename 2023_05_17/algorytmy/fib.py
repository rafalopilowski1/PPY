import sys

fibMemo = {}


def fib(n: int) -> int:
    """
    Calculates the n^th fibonacci number

    Parameters
    ----------
    n : int
        The n^th number from Fibonacci sequence

    Returns
    ----------
    number: int
        Nth fibonacci number
    """
    if n < 0:
        raise Exception("Incorrect number")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        if n not in fibMemo:
            fibMemo[n] = fib(n - 1) + fib(n - 2)
        return fibMemo[n]


def main():
    print(sys.argv)
    print(fib(int(sys.argv[1])))


if __name__ == "__main__":
    main()

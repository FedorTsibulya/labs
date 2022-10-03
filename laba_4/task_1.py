import sys
import argparse

def F(n):
    if n == 1 or n == 2:
        return 1
    return F(n-1) + F(n-2)

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int)
    parser.add_argument('number', nargs='?', type=int)
    return parser

if __name__ == '__main__':
    if len(sys.argv) > 3 or len(sys.argv) < 1:
        sys.exit("Ошибка ввода. Введите единственный аргумент N")
    parser = createParser()
    args = parser.parse_args()
    N = args.n
    if N is None:
        N = args.number
    print(F(N))    
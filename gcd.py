# Uses python3
import sys

def gcd(a, b):
    if b == 0:
      return a

    remainder = a % b

    return gcd (b, remainder)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
# Uses python3
import sys

def least_common_multiple(a, b):
  return (a*b) // greatest_common_divisor(a, b)

def greatest_common_divisor(a, b):
    if b == 0:
      return a

    remainder = a % b

    return greatest_common_divisor (b, remainder)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(least_common_multiple(a, b))
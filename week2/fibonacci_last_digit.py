# Uses python3
import sys

def get_fibonacci_last_digit(number):
  if number <= 1:
      return number

  sequence_tail = [0, 1, 1]

  for _ in range(3, number + 1):
    sequence_tail[0] = sequence_tail[1]
    sequence_tail[1] = sequence_tail[2]
    sequence_tail[2] = (sequence_tail[0] + sequence_tail[1]) % 10

  return sequence_tail[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    number = int(input)
    print(get_fibonacci_last_digit(number))
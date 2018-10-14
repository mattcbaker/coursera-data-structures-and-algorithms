# Uses python3
import sys

def get_fibonacci_modulo(fibonacci_number, modulo):
  remainder = fibonacci_number % get_pisano_period_length(modulo)

  return get_fibonacci_number(remainder) % modulo
  
def get_pisano_period_length(modulo):
  pisano_tail = [0, 1, 1]
  length = 0

  while True:
    pisano_tail[0] = pisano_tail[1]
    pisano_tail[1] = pisano_tail[2]
    pisano_tail[2] = (pisano_tail[0] + pisano_tail[1]) % modulo

    length += 1

    if pisano_tail[0] == 0 and pisano_tail[1] == 1:
      break

  return length

def get_fibonacci_number(number):
  if number <= 1:
      return number

  sequence_tail = [0, 1, 1]

  for _ in range(number - 1):
    sequence_tail[0] = sequence_tail[1]
    sequence_tail[1] = sequence_tail[2]
    sequence_tail[2] =  sequence_tail[0] + sequence_tail[1]

  return sequence_tail[1]

if __name__ == '__main__':
  input = sys.stdin.read()
  fibonacci_number, modulo = map(int, input.split())
  print(get_fibonacci_modulo(fibonacci_number, modulo))
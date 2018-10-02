# Uses python3
def calculate_fibonacci(number):
  if number <= 1:
      return number

  sequence_tail = [0, 1, 1]

  for _ in range(3, number + 1):
    sequence_tail[0] = sequence_tail[1]
    sequence_tail[1] = sequence_tail[2]
    sequence_tail[2] = sequence_tail[0] + sequence_tail[1]

  return sequence_tail[-1]

number = int(input())
print(calculate_fibonacci(number))
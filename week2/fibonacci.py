# Uses python3
def calculate_fibonacci(number):
  if number <= 1:
      return number

  tail_sequence = [0, 1, 1]

  for _ in range(3, number + 1):
    tail_sequence[0] = tail_sequence[1]
    tail_sequence[1] = tail_sequence[2]
    tail_sequence[2] = tail_sequence[0] + tail_sequence[1]

  return tail_sequence[-1]

number = int(input())
print(calculate_fibonacci(number))
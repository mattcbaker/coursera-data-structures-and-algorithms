# python3

def max_pairwise_product(integers):
  maximum_integers = [0] * 2

  for integer in integers:
    if integer > maximum_integers[0]:
      maximum_integers[1] = maximum_integers[0]
      maximum_integers[0] = integer 
    elif integer > maximum_integers[1]:
        maximum_integers[1] = integer

  return maximum_integers[0] * maximum_integers[1]
      
if __name__ == '__main__':
    input_length = int(input())
    input_integers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_integers))
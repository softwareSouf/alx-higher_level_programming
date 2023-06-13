#!/usr/bin/python3

def divisible_by_2(my_list=None):
  """Find all multiples of 2 in a list."""
  if my_list is None:
    my_list = []
  multiples = []
  for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
      multiples.append(my_list[i])
  return multiples

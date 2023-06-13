#!/usr/bin/python3

def multiple_returns(sentence):
  if sentence == "":
    length = 0
    first_character = None
  else:
    length = len(sentence)
    first_character = sentence[0]
  return length, first_character

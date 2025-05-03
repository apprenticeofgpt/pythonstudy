##답을 적어보시오
def hidden_word (words, slices):
  answer = ""
  for word, slice_list in zip(words, slices):
    for start, end in slice_list:
      answer += word[start:end+1]
  return answer
words = ["apocalypse","meteorology","architect","cheetah"]
slices = [[(1, 2), (5, 6)],[(2, 3)],[(2, 2)],[(1, 1)]]

print(hidden_word(words, slices))
import string
score=0
capitals = list(string.ascii_uppercase)
lower=list(string.ascii_lowercase)
numbers=[str(i) for i in range(10)]
password=input("input password: ")
def num_included(args):
  global score
  num_list=list(args)
  if any(chars in numbers for chars in num_list):
   score+=2
def over_eight(args):
  global score
  if len(args)>=8:
    score+=2
def cap_included(args):
  global score
  caplist=list(args)
  if any(chars in capitals for chars in caplist):
    score+=1
def word_included(args):
  global score
  lowlist=list(args)
  if any(chars in lower for chars in lowlist):
    score+=1

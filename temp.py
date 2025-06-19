import random

num = random.random()
with open('temp.txt', 'w') as w:
  w.write(str(num))

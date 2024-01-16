import random
def oneOutOfN(n):
  return random.randint(1,n) == 1

def maxValue(data):
  flippedList = []
  for key, val in data.items():
    flippedList.append((val, key))
  output = (max(flippedList)[1], max(flippedList)[0])
  return output

def minValue(data):
  flippedList = []
  for key, val in data.items():
    flippedList.append((val, key))
  output = flippedList
  return output

def averageValue(data):
  items = []
  for key, val in data.items():
    items.append(val)
  return sum(items)//len(items)

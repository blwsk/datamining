import numpy

# clean data
txt = open('entropyData.txt')
data = []
for line in txt:
  l = line.split(', ')
  l[1] = l[1].replace('\n', '')
  l[0] = float(l[0])
  l[1] = float(l[1])
  data.append(l)

def entropy(l):
  # expects 2-d array of [attr, class] format
  classes = []
  for item in l:
    if (item[1] not in classes):
      classes.append(item[1])

  classFreq = {}
  for c in classes:
    temp = 0
    for item in l:
      if item[1] == c:
        temp = temp + 1
    classFreq[c] = temp
  
  e = 0
  numItems = len(l)
  for item in l:
    cl = item[1]
    pij = float(float(classFreq[cl]) / float(numItems))
    e += pij * numpy.log2(pij)
  return -e
  

def shannon(a1, a2):
  e1 = entropy(a1)
  e2 = entropy(a2)
  totalNumEntries = len(a1) + len(a2)
  weightedAvg = (len(a1)*e1 + len(a2)*e2) / totalNumEntries
  return weightedAvg


def findSplits(d):
  num = len(d) - 1  # number of possible splits

  counter = 1
  # increment through the splits
  while(counter <= num):
    data1 = d[counter:]
    data2 = d[:counter]
    left = counter - 1
    right = counter
    print 'Entropy for split between ', left, ' and ', right, ': ', shannon(data1, data2)
    counter += 1

findSplits(data)
















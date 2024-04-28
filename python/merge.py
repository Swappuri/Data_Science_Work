# Assignment-7 - COSC 2316 - Professor McCurry
# Implemented by - Swapnil Puri

import math
import random
import matplotlib.pyplot as plt
import numpy as np

def main():
  global stepcounter

  # Plotting merge sort
  random.seed(5040)
  xs = list(range(1,100))
  ys = [check_steps(x) for x in xs]
  plt.plot(xs,ys)
  plt.title('Steps Required for Merge Sort for Random Lists')
  plt.xlabel('Number of Items in Random List')
  plt.ylabel('Steps Required to Sort List by Merge Sort')
  plt.show()

  # Generating curves
  ys_nlognb2 = [x * math.log2(x) for x in xs]
  ys_nlognb10 = [x * math.log(x) for x in xs]
  ys_exp = [math.exp(x) for x in xs]
  ys_squared = [x**2 for x in xs]
  ys_threehalves = [x**1.5 for x in xs]
  ys_cubed = [x**3 for x in xs]

  # Plotting all curves
  axes = plt.gca()
  axes.set_ylim([np.min(ys),np.max(ys) + 140])
  plt.plot(xs,ys)
  plt.plot(xs,ys_exp, label = "exp")
  plt.plot(xs,xs, label = "linear")
  plt.plot(xs,ys_squared, label = "x squared")
  plt.plot(xs,ys_cubed, label = "x cubed")
  plt.plot(xs,ys_threehalves, label = "x 1.5")
  plt.plot(xs,ys_nlognb10, label="x lg x base 10")
  plt.plot(xs,ys_nlognb2, label="x lg x base 2")
  plt.title('Comparing Merge Sort to Other Growth Rates')
  plt.xlabel('Number of Items in Random List')
  plt.ylabel('Steps Required to Sort List')
  leg = plt.legend(loc='lower right')
  print (stepcounter)
  plt.show()

# Generates an unsorted array and returns how many steps it took to sort it
def check_steps(size_of_cabinet):
  cabinet = [int(1000 * random.random()) for i in range(size_of_cabinet)]
  global stepcounter
  stepcounter = 0
  sortedcabinet = mergesort(cabinet)
  return (stepcounter)

# Combines two lists into a single sorted list
def merging(leftCabinet, rightCabinet):
  global stepcounter
  newCabinet = []
  # Iterates until a list is empty
  while (min(len(leftCabinet), len(rightCabinet)) > 0):
    # Finds the smaller digit from the lists to insert
    if (leftCabinet[0] > rightCabinet[0]):
      to_insert = rightCabinet.pop(0)
      newCabinet.append(to_insert)
      stepcounter += 1
    elif (leftCabinet[0] <= rightCabinet[0]):
      to_insert = leftCabinet.pop(0)
      newCabinet.append(to_insert)
      stepcounter += 1
  # Adds the rest of the remaining list
  if (len(leftCabinet) > 0):
    for i in leftCabinet:
      newCabinet.append(i)
  if (len(rightCabinet) > 0):
    for i in rightCabinet:
      newCabinet.append(i)
  return newCabinet

# Sorts a list by breaking it down and building it back up
def mergesort(cabinet):
  global stepcounter
  # Base case
  if (len(cabinet) == 1):
    newCabinet = cabinet
  # Creates two lists with half the elements of the given list and recursively iterates
  else:
    stepcounter += 1
    leftCabinet = mergesort(cabinet[:math.floor(len(cabinet) / 2)])
    rightCabinet = mergesort(cabinet[math.floor(len(cabinet) / 2):])
    newCabinet = merging(leftCabinet, rightCabinet)

  return (newCabinet)

if __name__ == "__main__":
  main()
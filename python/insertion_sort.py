# Inclass Assignment-4 - COSC 2316 - Professor McCurry
# Implemented by - Swapnil Puri
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import math
import numpy as np

# Inserts a number into the correct position in an ascending order array
def insert_cabinet(cabinet,to_insert):
  check_location = len(cabinet) - 1
  insert_location = 0
  global stepcounter

  # Iterates through the cabinet array
  while(check_location >= 0):
    stepcounter += 1

    # Sets the insert location to one index behind the first number smaller than the inserted number
    if to_insert > cabinet[check_location]:
      insert_location = check_location + 1
      check_location = - 1
    check_location = check_location - 1
    stepcounter += 1

  # Insert number and return new cabinet
  cabinet.insert(insert_location,to_insert)
  return(cabinet)

# Creates a new sorted cabinet when given an unsorted one
def insertion_sort(oldCabinet):
  newCabinet = []
  global stepcounter

  # Iterates while the unsorted cabinet still has elements
  while len(oldCabinet) > 0:
    stepcounter += 1

    # Take out elements from the unsorted array and insert them into the correct position in a sorted array
    to_insert = oldCabinet.pop(0)
    newCabinet = insert_cabinet(newCabinet, to_insert)
    stepcounter += 1

  return(newCabinet)

# Generates an unsorted array of a certain size and returns how many steps it took to sort it
def check_steps(size_of_cabinet):
  cabinet = [int(1000 * random.random()) for i in range(size_of_cabinet)]
  global stepcounter
  stepcounter = 0
  start = timer()
  sortedcabinet = insertion_sort(cabinet)
  end = timer()
  return(end - start) * 10000000

cabinet = [8,4,6,1,2,5,3,7]
print ("Old unsorted Cabinet:", cabinet, "\n")

# Displays a sorted cabinet and the number of steps it took to sort it
stepcounter = 0
sortedCabinet = insertion_sort(cabinet)
print("Sorted Cabinet:",sortedCabinet)
print("Number of steps:", stepcounter)

end = timer()

# Generates and plots the relationship between the number of files and the number steps required to sort them via insertion sort
random.seed(5040)
xs = list(range(1,100))
ys = [check_steps(x) for x in xs]
print(ys)
plt.plot(xs,ys)
plt.title('Steps Required for Insertion Sort for Random Cabinets')
plt.xlabel('Number of Files in Random Cabinet')
plt.ylabel('Steps Required to Sort Cabinet by Insertion Sort')
plt.show()

# Generates the number of steps required given the size of the input for several functions
random.seed(5040)
xs = list(range(1,100))
ys = [check_steps(x) for x in xs]
ys_exp = [math.exp(x) for x in xs]
ys_squared = [x**2 for x in xs]
ys_threehalves = [x**1.5 for x in xs]
ys_cubed = [x**3 for x in xs]

# Plots the relationship between the number of files and the number steps required for several functions
plt.plot(xs,ys)
axes = plt.gca()
axes.set_ylim([np.min(ys),np.max(ys) + 140])
plt.plot(xs,ys_exp, label = "exp")
plt.plot(xs,xs, label = "linear")
plt.plot(xs,ys_squared, label = "x squared")
plt.plot(xs,ys_cubed, label = "x cubed")
plt.plot(xs,ys_threehalves, label = "x 1.5")

# Provides critical information about the graph
leg = plt.legend(loc='upper center')
plt.title('Comparing Insertion Sort to Other Growth Rates')
plt.xlabel('Number of Files in Random Cabinet')
plt.ylabel('Steps Required to Sort Cabinet')
plt.show()
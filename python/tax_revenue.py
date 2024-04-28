# Inclass Assignment-3 - COSC 2316 - Professor McCurry
# Implemented by - Swapnil Puri

import math
import matplotlib.pyplot as plt

# determines the revenue made based on a tax rate
def revenue(tax):
  return (100 * (math.log(tax + 1) - (tax - 0.2) ** 2 + 0.04))

# finds the slope of the tangent line of a point
def revenue_derivative(tax):
  return (100 * (1 / (tax + 1) - 2 * (tax - 0.2)))

# creates a graph that displays the relationship between tax rate and revenue
def tax_plot(tax):
  xs = [x / 1000 for x in range(1001)]
  ys = [revenue(x) for x in xs]
  plt.plot(xs, ys)
  plt.title('Tax Rates and Revenue')
  plt.xlabel('Tax Rate')
  plt.ylabel('Revenue')
  plt.plot(tax, revenue(tax), 'ro')
  plt.show()

# determines the tax rate that results in the most revenue
def max_revenue(step_size, threshold, maximum_iterations, iterations, current_rate):
  keep_going = True
  while(keep_going):

    # move the current_rate closer to maximum rate by adding the product of a specific step size and the derivative at the current point
    rate_change = step_size * revenue_derivative(current_rate)
    current_rate += rate_change

    # stop if the absolute value of the rate of change is within the threshold
    if(abs(rate_change) < threshold):
      keep_going = False

    # stop if the number of times the while loop has run is greater than the maximum number allowed
    if(iterations >= maximum_iterations):
      keep_going = False

    iterations += 1

  return current_rate

def main():
  # plotting the revenue function
  current_rate = 0.7
  tax_plot(current_rate)
  print("Revenue derivative before maximizing:", revenue_derivative(current_rate))

  # defining the variables for the max_revenue function
  step_size = 0.001
  threshold = 0.0001
  maximum_iterations = 100000
  iterations = 0

  # calling the max_revenue function
  max_rate = max_revenue(step_size, threshold, maximum_iterations, iterations, current_rate)

  # plotting the revenue function after maximizing
  tax_plot(max_rate)

  # outputting the results
  print ("Revenue derivative after maximizing: ", revenue_derivative(max_rate))
  print ("Maximized tax rate: ", max_rate)
  print ("Maximized revenue: ", revenue(max_rate))

if __name__ == '__main__':
  main()
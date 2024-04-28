from timeit import default_timer as time
import matplotlib.pyplot as plt

def main():
  start = time()
  # before reaching minima
  current_x = -850
  plot_graph(current_x)
  print ("\nDerivative of current point before minimizing:", find_cost_derivative(current_x), "\n")

  step_size = 0.001
  threshold = 0.0001
  max_iteration = 5000

  # after reaching minima
  new_x = gradient_descent(current_x, step_size, threshold, max_iteration)
  plot_graph(new_x)
  print ("Derivative of new point after minimizing", find_cost_derivative(new_x), "\n")

  # outputs the coordinates of the absolute/relative minima found
  print ("Minimized x:", new_x)
  print ("Minimized cost:", find_cost(new_x), "\n")
  end = time()

  print (end - start)

# determines the cost based on x
def find_cost(x):
  return (x + 764)**2 + 3 * x - 500

# determines the derivative at a point based on x
def find_cost_derivative(x):
  return 2 * (x + 764) + 3

# locates the nearest absolute or relative minima
def gradient_descent(current_x, step_size, threshold, max_iteration):
  keep_going = True
  iteration = 0

  while (keep_going):
    # subtract the rate of change from the current value of x
    rate_of_change = step_size * find_cost_derivative(current_x)
    current_x -= rate_of_change

    # determine if the rate of change is within the specified threshold
    if (abs(rate_of_change) < threshold):
      keep_going = False

    # determine if too many steps were taken based on a given limit
    if (iteration >= max_iteration):
      keep_going = False

    iteration += 1

  return current_x

# creates a graph that displays the relationship between x and cost
def plot_graph(current_x):
  x = [x for x in range(-1030, -500)]
  y = [find_cost(val) for val in x]

  plt.plot(x, y)
  plt.plot(current_x, find_cost(current_x), 'ro')
  plt.title("Gradient Descent")
  plt.xlabel("x-axis")
  plt.ylabel("Cost")
  plt.show()

if __name__ == "__main__":
  main()

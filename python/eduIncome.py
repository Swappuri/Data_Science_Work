import math
import matplotlib.pyplot as plt

# determine income based on years of education
def income(edu_yrs):
  return(math.sin((edu_yrs - 10.6) * (2 * math.pi / 4)) + (edu_yrs - 11) / 2)

# determine the derivative at a specific point based on years of education
def income_derivative(edu_yrs):
  return(math.cos((edu_yrs - 10.6) * (2 * math.pi / 4)) + 1/2)

# graph relationship between years of education and income
def EduIncomePlt(edu_yrs):
  xs = [11 + x/100 for x in list(range(901))]
  ys = [income(x) for x in xs]
  plt.plot(xs, ys)
  plt.plot(edu_yrs, income(edu_yrs), 'ro')
  plt.title('Education and Income')
  plt.xlabel('Years of Education')
  plt.ylabel('Lifetime Income')
  plt.show()

# find the local maximum based on current years of education
def find_extrema(current_edu):
  # define variables to find local maximum
  threshold = 0.0001
  maximum_iterations = 100000
  step_size = 0.001
  keep_going = True
  iterations = 0

  while(keep_going):
    # add rate of change to the current years of education
    education_change = step_size * income_derivative(current_edu)
    current_edu = current_edu + education_change

    # check if the rate of change is within a specific threshold
    if(abs(education_change) < threshold):
        keep_going = False

    # check if the while loop has iterated too many times
    if(iterations >= maximum_iterations):
        keep_going = False

    iterations += 1

  return current_edu

# print plot and derivative prior to finding the local maximum
current_edu = 12.5
EduIncomePlt(current_edu)
print("Education/Income derivative before maximizing: ", income_derivative(current_edu), "\n")

# find and print first maximum
extreme = find_extrema(current_edu)
print("Maximized number of years of education ", extreme, "\n")
EduIncomePlt(extreme)
print("Education/Income derivative after maximizing: ", income_derivative(extreme))

# find and print second maximum
current_edu = 14
extreme = find_extrema(current_edu)
print("Maximized number of years of education ", extreme, "\n")
EduIncomePlt(extreme)
print("Education/Income derivative after maximizing: ", income_derivative(extreme))

# find and print third maximum
current_edu = 18
extreme = find_extrema(current_edu)
print("Maximized number of years of education ", extreme, "\n")
EduIncomePlt(extreme)
print("Education/Income derivative after maximizing: ", income_derivative(extreme))

# find and print a point off of the graph
current_edu = 2
extreme = find_extrema(current_edu)
print("Maximized number of years of education ", extreme, "\n")
EduIncomePlt(extreme)
print("Education/Income derivative after maximizing: ", income_derivative(extreme))

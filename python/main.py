
def main():
  print(euclid(776, 6))


def euclid(num1, num2):
  try:
    minimum = min(num1, num2)
    maximum = max(num1, num2)

    remainder = maximum % minimum

    if(remainder == 0):
      return minimum
    elif(remainder != 0):
      return euclid(minimum, remainder)
  except RecursionError:
    print("Invalid")

main()
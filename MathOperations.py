import math
#Main function:
def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)

def even_checker(n):
    if n%2 == True:
        return "Number is Even"
    else:
        return "Number is Odd"

#Testing:
nums = [0,1,6,13, 23]
for i in nums:
  print("My function factorial of {}: {} compared to math library: {}".format(i,factorial(i),math.factorial(i)))

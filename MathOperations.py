import math
#Main function:
def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)

#Testing:
nums = [0,1,6,13, 23]
for i in nums:
  print("My function factorial of {}: {} compared to math library: {}".format(i,factorial(i),math.factorial(i)))

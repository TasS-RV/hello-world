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


#2nd part of progrma using Dictionaries:

#Names to abreviations, then reversal into a dictionary - and print them into a sorted list
name_ab = {"Corpus Christi": "CC", "Magdalene":"M", "Trinity":"T", "Clare":"C", "Lucy Cavendish":"LC", "Gonville and Caius":"CAI", "Queens":"Q", "Sidney Sussex":"SID", "Pembroke":"PEM",}
ab_name = {}

for key in name_ab:
  ab_name[name_ab[key]] = key  #Abbreviation: Name (reversal form initial)

#Abbreviations: names - reversed order dictionary
print(ab_name)

abb_ = [key_val for key_val in ab_name]

#Sorted by alphabetical order (if otherwise specified by sorted(array_name, key = lambda function or reverse))
abb_ = sorted(abb_)

print("Sorted list of college abbreviations: ",abb_)

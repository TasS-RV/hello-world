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


#2nd part of program using Dictionaries:

#Initiate the while loop
state = "Y"

while state != "N":

    #List of colleges - unsorted and not in order
    name_ab = {"Corpus Christi": "CC", "Magdalene":"M", "Trinity":"T", "Clare":"C", "Lucy Cavendish":"LC", "Gonville and Caius":"CAI", "Queens":"Q", "Sidney Sussex":"SID", "Pembroke":"PEM",}
    ab_name = {}
    
    #Names to abreviations, then reversal into a dictionary - and print them into a sorted list
    in_abbr, in_name = str(input("Please enter the abbreviation and name of the college you would like to add: (abbr, name)")).split(',')
    name_ab[in_name] = in_abbr 
    state = str(input("Add details of another college Y/N?")) #Repeats the loop if user wants to add another college

    for key in name_ab:
        ab_name[name_ab[key]] = key  #Abbreviation: Name (reversal form initial)

#Abbreviations: names - reversed order dictionary
    print(ab_name)

    abb_ = [key_val for key_val in ab_name]

#Sorted by alphabetical order (if otherwise specified by sorted(array_name, key = lambda function or reverse))
    abb_ = sorted(abb_)

    print("Sorted list of college abbreviations: ",abb_)

#Problem with above while loop - messy to print out the whole sorted list for each college addition one by one
#Build in separate while iteration in a sub-program: to collect all colleges and parse into overall dict.
    

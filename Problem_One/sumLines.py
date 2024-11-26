# Matthew Dingman
# Professor Qouneh

# This script is used to read a text file and compute the sum, number of
# integers, and the average of all the numbers.

# Example invocation: python3 sumLines.py
import sys

file = sys.argv[1] # Declare the input file as the given argument
with open(file, "r") as file: # Open input file, declare as file
  numbers = []  # Declare numbers as an empty list
  sum = 0 # Declare sum as int 0
  for line in file: # Split the numbers by line into list, append to numbers list by individual number per index
    nums = line.split()
    for i in nums:
      sum = sum + int(i)  # Add every number together, save as sum variable
      numbers.append(i)
length = len(numbers) # Save length of numbers as length
avg = sum/length # Save average as avg

print(f"Sum: {sum}\nAvg: {avg}\nLength: {length}")

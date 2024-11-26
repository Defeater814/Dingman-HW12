# Matthew Dingman
# Professor Qouneh

# This script is used to read two input text files and reconstruct/combine their
# contents to produce complete output.

# Example invocation: python3 reconstructSentence.py

file1 = "input1.txt"    # Define file names as variables
file2 = "input2.txt"
outfile = "output.txt"
content_rv = []         # Declare content_rv as an empty list
with open(file1, "r") as file1: # Open input1.txt as variable file1
  for line in file1:
    content = line.split()  # Make a list of the words in input1.txt
    for i in range(len(content)): # Reverse the list, save as reverse_1
      content_rv.append(content[-1-i])
      reverse_1 = content_rv
content_rv = [] # Re-declare content_rv as empty list
with open(file2, "r") as file2: # Open input2.txt as variable file2
  for line in file2:
    content = line.split() # Make a list of the words in input2.txt
    for i in range(len(content)): # Reverse the list, save as reverse_2
      content_rv.append(content[-1-i])
      reverse_2 = content_rv
sentence = str() # Declare sentence as a string

if len(reverse_1) > len(reverse_2): # Set the iteration value to the larger len
  x = len(reverse_1)
else:
  x = len(reverse_2)
if x%2 == 1: # Check for an odd iteration number, as that means reverse_1 will have more indexes
  for i in range(x):
    sentence = sentence + reverse_1[i] + " "
    sentence = sentence + reverse_2[i] + " "
  print(sentence)
else:
  for i in range(x-1):
    sentence = sentence + reverse_1[i] + " "
    sentence = sentence + reverse_2[i] + " "
  sentence = sentence + reverse_1[i+1]
  print(sentence)
with open(outfile, "w") as outfile: # Save final fixed sentence to outputfile.txt
  outfile.write(sentence)

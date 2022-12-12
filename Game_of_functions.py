# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def summation(Sample_List):
    sum=0
    for i in Sample_List:
      sum+=i
    return sum
Sample_List=[8, 2, 3, 0, 7]
print("Output is :", summation(Sample_List))
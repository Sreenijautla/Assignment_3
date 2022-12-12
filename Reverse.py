# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"


def reverse(string1):
    string2=''
    for i in string1:
        string2=i+string2
    return string2
string1="1234abcd"
print("Reversed string is :", reverse(string1))
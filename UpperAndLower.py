# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def upperlower(string):
	u=0
	l=0
	for i in range(len(string)):
		if (ord(string[i])>=97 and ord(string[i])<=122):
			l+=1
		elif (ord(string[i])>=65 and ord(string[i])<=90):
			u+=1
	print("No. of Upper case characters :", u)
	print("No. of Lower case Characters :", l)
string='The quick Brow Fox'
upperlower(string)
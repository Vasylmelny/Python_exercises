# Capitalize the  first letter of each word in a string

string = input("Enter a string: ")
arr = string.split(" ")
arr1 = []

# string1 = ""
for i in arr:
    i = i.capitalize()
    arr1.append(i)

string1 = " ".join(arr1)
print(string1)
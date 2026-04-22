# Practice Problem: Write a program to capitalize the first letter
# of each word in a given string without using the built-in .title() method.

text = "hello world from python"

lst = text.split()
for word in lst:
    print(word.capitalize(), end=" ")

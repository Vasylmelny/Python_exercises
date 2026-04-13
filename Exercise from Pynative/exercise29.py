# Create a list of 5 words. Write a loop that iterates through the list
# and prints each word alongside its character count.

words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

for word in words:
    n = len(word)
    print(f"{word} - {n}")
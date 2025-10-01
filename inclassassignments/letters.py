word = input("Enter a word: ")
letter = input("Enter the letter to count: ")
count = 0

for char in word:
    if char == letter:
        count += 1

print(f"{letter} appears {count} times.")
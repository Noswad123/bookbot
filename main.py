import sys

# book_path = "books/frankenstein.txt"
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]  # Fix: Correct usage of sys.argv
with open(book_path) as f:
    contents = f.read()
word_count = len(contents.split())

letter_dict = {}
for letter in contents:
    lowercase = letter.lower()
    if lowercase not in letter_dict:
        letter_dict[lowercase] = 0
    letter_dict[lowercase] += 1

print(f"-- Begin report of {book_path} --")
print(f"{word_count} words found in the document ")
print("\n")

for key,val in letter_dict.items():
    print(f"{key}: {val}")

print(f"-- End report--")

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Words with an odd number of characters:")
for word in odd_length_words:
    print(word)
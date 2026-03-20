import string

word_counts = {}

with open("input.txt", "r") as file:
    text = file.read().lower()

# Remove punctuation
for char in string.punctuation:
    text = text.replace(char, "")

words = text.split()

# Ignore common words
ignore_words = {"the", "is", "and", "a", "to", "of"}

# Count words
for word in words:
    if word not in ignore_words:
        word_counts[word] = word_counts.get(word, 0) + 1

# Sort words by count (highest first)
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Show top 5
print("\nTop 5 words:")
for word, count in sorted_words[:5]:
    print(f"{word}: {count}")

# Write to file
with open("output.txt", "w") as file:
    for word, count in sorted_words:
        file.write(f"{word}: {count}\n")

print("Improved word count complete!")


import sys
from collections import Counter

# Get the file name
filename = sys.argv[1]

# Get the word from the command-line argument
word = sys.argv[2]

# Open the file and read all lines
with open(filename) as f:
    lines = f.readlines()

# Print the total number of lines
print("Total lines:", len(lines))

# Create a Counter
counts = Counter()

# Check each line
for line in lines:
    fields = line.split()

    # Count the word if it appears in the line
    for field in fields:
        if field == word:
            counts[field] += 1

# Print the result
print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)

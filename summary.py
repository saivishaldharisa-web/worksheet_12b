
import sys
from collections import Counter

# Get the file name from the command-line argument
filename = sys.argv[1]

# Open the file and read all lines
with open(filename) as f:
    lines = f.readlines()

# Print the total number of lines in the file
print("Total lines:", len(lines))

# Create a Counter to count the occurrences of each item
counts = Counter()

# Go through each line in the file
for line in lines:
    # Split the line into separate fields
    fields = line.split()

    # Check if the line has more than 7 fields
    if len(fields) > 7:
        # Get the 8th field (index 7)
        key = fields[7]

        # Increase the count of this field by 1
        counts[key] += 1

# Print the heading for the top 5 items
print("Top 5:")

# Display the 5 most frequently occurring items
for item, n in counts.most_common(5):
    print(item, n)

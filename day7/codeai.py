
# Import the os and re modules
import os
import re

# Define a regular expression pattern for matching directory names
pattern = r"^dir\s+(\S+)"

# Initialize a dictionary to store the sizes of the directories
directory_sizes = {}

# Initialize the directory stack to an empty list
directory_stack = []

# Open the text file for reading
with open("input.txt", "r") as f:
    # Read each line from the file
    for line in f:
        # Check if the line contains a "cd" command
        if line.startswith("$ cd "):
            # Extract the target directory from the command
            target_dir = line[5:].strip()

            # If the target directory is "..", move up one level in the directory tree
            if target_dir == "..":
                if len(directory_stack) > 0:
                    directory_stack.pop()

            # Otherwise, add the target directory to the directory stack
            else:
                directory_stack.append(target_dir)

        # Check if the line contains an "ls" command
        elif line.startswith("$ ls"):
            # Extract the current directory from the top of the directory stack
            current_dir = directory_stack[-1]

            # Read the rest of the lines in the file until we reach the end of the listing
            listing = []
            for next_line in f:
                if not next_line.startswith("$ "):
                    listing.append(next_line)
                else:
                    break

            # Join the lines of the listing into a single string
            listing_str = "\n".join(listing)

            # Use the regular expression to find all the directory names in the listing
            for match in re.finditer(pattern, listing_str):
                # Extract the directory name from the match
                dir_name = match.group(1)

                # Compute the full path of the directory
                dir_path = os.path.join(current_dir, dir_name)

                # Initialize the size of the directory to zero
                directory_sizes[dir_path] = 0

        # Check if the line contains a file with a numeric size
        elif line.endswith(".txt") or line.endswith(".dat") or line.endswith(".lst") or line.endswith(".log") or line.endswith(".ext"):
            # Extract the size of the file from the line
            size = int(line.split()[-2])

            # Compute the full path of the file's directory
            dir_path = os.path.join(*directory_stack)

            # Add the size of the file to the directory's size
            directory_sizes[dir_path] += size

# Print the sizes of all the directories

for dir_path, size in directory_sizes.items():
    print(f"{dir_path}: {size} bytes")
import sys

# Step 1: Check if exactly one argument is given
if len(sys.argv) != 2:
    sys.exit("You must provide exactly one Python file as input.")

filename = sys.argv[1]

# Step 1 continued: Check if it ends with .py
if not filename.endswith(".py"):
    sys.exit("The file must end with .py")

# Step 1 continued: Try to open the file to see if it exists
try:

    with open(filename) as file:
# Step 2: Count the real lines of code
        count = 0
        for line in file:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            count += 1
# Step 1 contingency
except FileNotFoundError:
    sys.exit("The file does not exist.")

print(f"Lines of code: {count}")
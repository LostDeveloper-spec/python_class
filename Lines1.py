import sys

def main():
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    # Check if the file ends with .py
    if not filename.endswith(".py"):
        sys.exit("Error: Not a Python file.")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            count = 0
            for line in file:
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue
                count += 1

        print(count)

    except FileNotFoundError:
        sys.exit("Error: File does not exist.")
    except Exception as e:
        sys.exit(f"Error: {e}")

if __name__ == "__main__":
    main()
import csv
import sys

def main():
# Ensure the correct num of arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
# Get stuff from the input file
        with open(input_file, mode="r", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            students = []

            for row in reader:
                try:
                    last, first = row["name"].split(", ")
                    students.append({
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    })
                except ValueError:
                    sys.exit("Error: Invalid name format in input file.")
    except Exception:
        sys.exit("Error: Something went wrong. Try Fixing your name format in the input file")
# Write cleaned data to the output CSV file
        with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)

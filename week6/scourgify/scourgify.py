import sys
import csv

# check arguments
if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()

        next(reader)  # skip old header row

        for row in reader:
            name, house = row
            last, first = name.split(", ")
            writer.writerow({"first": first, "last": last, "house": house})

except FileNotFoundError:
    print(f"Could not read {input_file}")
    sys.exit(1)

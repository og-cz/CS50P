score = 85

# Best way to read expressions:
# Left to right, keeping the symbols and sides exactly as written, and then reason about the truth of the comparison.

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 90:
    print("B")
elif 70 <= score <= 80:
    print("C")
elif 60 <= score <= 70:
    print("D")
else:
    print("Fail")

# better way to do

if 90 >= score:
    print("A")
elif 80 >= score:
    print("B")
elif 70 >= score:
    print("C")
elif 60 >= score:
    print("D")
else:
    print("Fail")

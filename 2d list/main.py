# phone keypad demo

no_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for row in no_pad:
    for no in row:
        print(no, end=" ")
    print()

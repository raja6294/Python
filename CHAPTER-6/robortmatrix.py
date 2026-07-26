grid = [["A1", "A2"], ["B1", "B2"]]
for row in grid:
    for item in row:
        if item == "A2":
            break  # Escapes inner loop only
        print(item, end=" ")
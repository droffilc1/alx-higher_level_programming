#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        print(f"{i}{j}", end=", " if not (i == 8 and j == 9) else "")
print()

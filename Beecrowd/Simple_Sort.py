a, b, c = map(int, input().split())
original = [a, b, c]
sorted_values = sorted(original)
for value in sorted_values:
    print(value)
print()
for value in original:
    print(value)
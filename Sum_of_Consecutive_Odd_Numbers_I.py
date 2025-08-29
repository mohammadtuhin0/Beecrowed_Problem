X = int(input())
Y = int(input())

small = min(X, Y)
large = max(X, Y)
total = 0

for num in range(small+1, large):
    if num % 2 != 0:
        total += num
print(total)
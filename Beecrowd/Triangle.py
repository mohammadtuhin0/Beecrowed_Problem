A, B, C = map(float, input().split())
if A < B + C and B < A + C and C < B + C:
    perimeter = A + B + C
    print(f"Perimetro = {perimeter:.1f}")
else:
    area = ((A + B) * C) / 2
    print(f"Area = {area:.1f}")
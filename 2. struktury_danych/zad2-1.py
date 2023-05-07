krotka = (10, -3, 4, 9, 12, -6, 0)

max = krotka[0]
min = krotka[0]

for num in krotka[1:]:
    if num > max:
        max = num
    if num < min:
        min = num

print("Największa liczba w krotce to:", max)
print("Najmniejsza liczba w krotce to:", min)
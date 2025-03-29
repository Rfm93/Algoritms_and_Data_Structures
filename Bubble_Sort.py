
# Algoritm Bubble Sort

n = [45, 12, 78, 34, 23, 89, 56, 90, 11, 67, 22, 39, 81, 71, 6, 15, 37, 63, 99, 28]

i = 0

j = 0


# the variable i represents the number of passes of the outer loop
while i <= len(n):
# The j variable goes through the array to make the element changes in the inner loop.
    while j <= len(n) - 2:
        if n[j] > n[j + 1]:
            n[j], n[j + 1] = n[j + 1], n[j]
            j += 1
        j += 1 
    j = 0
    i += 1
print(n)









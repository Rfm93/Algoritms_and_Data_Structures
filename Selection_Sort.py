# Selection Sort

n = [45, 12, 78, 34, 23, 89, 56, 90, 11, 67, 22, 39, 81, 71, 6, 15, 37, 63, 99, 28]

i = 0

j = 1

s = n[i]


while i < len(n):
    s = n[i]
    # 1. Find the smallest element in the data set.
    while j <= len(n)-1:
        if s > n[j]:
            s = n[j]
            j += 1
        j += 1
    s = n.index(s)
    # 2. Swap the smallest element with the first element of the list
    n[s], n[i] = n[i], n[s]
    # 3. Repeat the process for the remaining subarrays, ignoring the already sorted elements.
    i += 1
    j = i
    

print(n)

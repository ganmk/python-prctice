import sys
array = [1,2,3,6,5,4]
for i in range(len(array)):
    for j in range(i):
        if array[j] > array[i]:
            array[j], array[i] = array[i], array[j]
print array

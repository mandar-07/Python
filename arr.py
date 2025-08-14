cars=["toyota","suzuki","volvo","bmw"]
for car in cars:
    print(car)
length=len(cars)
print("Number of cars:",length)



arr = [5, 3, 8, 1, 3]

print("Original array:", arr)

arr.append(10)
print("After append(10):", arr)

arr.extend([20, 30])
print("After extend([20, 30]):", arr)

arr.insert(2, 99)
print("After insert(2, 99):", arr)

arr.remove(3)
print("After remove(3):", arr)

popped = arr.pop()
print("After pop():", arr, "| Popped value:", popped)

popped_index = arr.pop(1)
print("After pop(1):", arr, "| Popped value at index 1:", popped_index)



count_3 = arr.count(3)
print("Count of 3:", count_3)

arr.sort()
print("After sort():", arr)

arr.reverse()
print("After reverse():", arr)

arr_copy = arr.copy()
print("Copy of the array:", arr_copy)

arr.clear()
print("After clear():", arr)

arr2 = [2, 4, 6, 8]
print("New array for utility functions:", arr2)
print("Length:", len(arr2))
print("Max:", max(arr2))
print("Min:", min(arr2))
print("Sum:", sum(arr2))
print("Sorted:", sorted(arr2))
print("Reversed (iterator to list):", list(reversed(arr2)))

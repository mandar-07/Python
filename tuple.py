empty_tuple = ()
single_element_tuple = (42,)
multiple_elements_tuple = (1, 2, 3, 2, 4, 2)

print("Empty tuple:", empty_tuple)
print("Single element tuple:", single_element_tuple)
print("Multiple elements tuple:", multiple_elements_tuple)

count_2 = multiple_elements_tuple.count(2)
print("\nCount of 2 in multiple_elements_tuple:", count_2)

index_3 = multiple_elements_tuple.index(3)
print("Index of 3 in multiple_elements_tuple:", index_3)



print("\nAccess element at index 0:", multiple_elements_tuple[0])
print("Slice from index 1 to 4:", multiple_elements_tuple[1:4])
print("Concatenate tuples:", multiple_elements_tuple + (5, 6))
print("Repeat tuple:", single_element_tuple * 3)

print("\nIterate over multiple_elements_tuple:")
for item in multiple_elements_tuple:
    print(item)

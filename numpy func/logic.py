import numpy as np 
print("\nLogical & Comparison:\n")

arr = np.array([1, 2, 3, 4, 5])

condition = arr > 3
print("Condition (arr > 3):", condition)

indices = np.where(condition)
print("Indices where condition is True:", indices)

print("Any > 3?", np.any(condition))
print("All > 0?", np.all(arr > 0))

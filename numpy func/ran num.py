import numpy as np

print("\nRandom Number Generation:\n")

rand_nums = np.random.rand(3)
print("Random numbers (0 to 1):", rand_nums)

rand_ints = np.random.randint(10, 20, size=5)
print("Random integers between 10 and 20:", rand_ints)

rand_normals = np.random.normal(0, 1, 4)
print("Random numbers with normal distribution (mean=0, std=1):", rand_normals)



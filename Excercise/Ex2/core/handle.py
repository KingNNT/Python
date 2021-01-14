import numpy as np
import random as random

m = 5
n = 7

def main():
	arr = np.zeros((m, n), dtype="int")
	for i in range(m):
		for j in range(n):
			arr[i, j] = random.randint(0,9)

	sum = 0

	for i in range(m):
		for j in range(n):
			print(arr[i, j])
			sum += arr[i,j]

	min = max = arr[0, 0]
	for i in range(m):
		for j in range(n):
			if min > arr[i, j]:
				min = arr[i, j]
			if max < arr[i, j]:
				max = arr[i, j]
	print("Min = ", min, " - Max = ", max)
	print("Sum = ", sum)
	print("AVG = ", sum/(arr.shape[0] + arr.shape[1]))

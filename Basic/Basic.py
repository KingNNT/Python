import numpy as np
import random as random

n = 10

def main():
	arr = np.zeros(n, dtype="int")
	for i in range(n):
		arr[i] = random.randint(0, 9)
	
	sum = 0
	for i in range(n):
		print(arr[i])
		sum += arr[i]
	print("Sum of array is: ", sum)


""" Solve """
if __name__ == "__main__":
	main()
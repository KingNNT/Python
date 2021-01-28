import numpy as np
import codecs
import sys

sys.stdin = codecs.getreader('utf-8')(sys.stdin)

def main():
	a = []
	for i in range(5):
		print("Nhập Số Nguyên: ")
		sz = input()
		t = int(sz)
		a.append(t)
	print("Danh sách a có số phần tử là: ", len(a))
	print("Danh sách a là: ", a)

if __name__ == "__main__":
	main()
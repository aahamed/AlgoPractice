# def sansa_xor(array):
	# final_res = 0
	# n = len(array)
	# for i in range(1, n + 1):
		# for j in range(0, n - i + 1):
			# inner_res = 0
			# for k in range(0, i):
				# inner_res = inner_res ^ array[j + k]
			# final_res = final_res ^ inner_res
	# return final_res
	
def sansa_xor_1(array):
	final_res = 0
	n = len(array)
	inner_res = [0 for i in range(n)]
	for i in range(1, n + 1):
		for j in range(0, n - i + 1):
			inner_res[j] = inner_res[j] ^ array[j + i - 1]
			final_res = final_res ^ inner_res[j]
	return final_res
	
def sansa_xor_2(array):
	n = len(array)
	print(n)
	if(n % 2 == 0):
		return 0
	else:
		return array[0] ^ array[n-1]


def test1():
	a = [1, 2, 3]
	print("res:", sansa_xor_1(a))
	a = [4, 5, 7, 5]
	print("res:", sansa_xor_2(a))
	a = [4, 5, 7, 5, 1, 2, 3, 4, 4, 5, 7, 5, 2, 8, 9, 121, 23, 87, 95]
	print("res_1:", sansa_xor_1(a))
	print("res_2:", sansa_xor_2(a))
	
	
	
def main():
	test1()
	
if __name__ == "__main__":
	main()
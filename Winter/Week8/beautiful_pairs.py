def beautiful_pairs(A, B):
	count = 0
	N = len(A)
	# construct map for B
	b_map = {}
	for i in range(N):
		if B[i] in b_map:
			b_map[B[i]].append(i)
		else:
			b_map[B[i]] = [i]
	
	# create flag arrays
	flag_a = []
	flag_b = []
	for i in range(N):
		flag_a.append(False)
		flag_b.append(False)
	
	# Find beautiful pairs
	for i in range(N):
		if A[i] in b_map:
			flag_a[i] = True
			b_index = b_map[A[i]].pop()
			flag_b[b_index] = True
			# delete key from b_map if list is empty
			if len(b_map[A[i]]) == 0:
				b_map.pop(A[i])
			count += 1
			
	# Find a pair of indices that are not beautiful
	# a_index = b_index = 0
	# for i in range(N):
		# if not(flag_a[i]):
			# a_index = i
		# if not(flag_b[i]):
			# b_index = i
	
	for i in range(N):
		if not(flag_a[i]):
			return count+1
	return count


def test_bpairs():
	A = [1, 2, 2, 3, 10, 12]
	B = [1, 2, 3, 4, 6, 5]
	print("num pairs =", beautiful_pairs(A, B))
	
def main():
	test_bpairs()
	
if __name__ == "__main__":
	main()
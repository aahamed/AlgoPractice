class BearPaints(object):
	
	def __init__(self):
		pass
		
	def max_area(self, W, H, M):
		max = 0
		res = 0
		for i in range(1, W+1):
			for j in range(min(i, H), H+1):
				prod = i*j
				if prod > max and prod <= M:
					res = (i, j)
					max = i*j
		print('res:', res)
		return max
		
def main():
	bp = BearPaints()
	print('max:', bp.max_area(4, 4, 10))
	print('max:', bp.max_area(3, 5, 14))
	# print('max:', bp.max_area(100000, 12345, 1000000000000))
	print('max:', bp.max_area(1000000, 1000000, 720000000007))
	
if __name__ == '__main__':
	main()
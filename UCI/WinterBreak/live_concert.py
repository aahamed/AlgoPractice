"""
live_concert.py: topcoder problem
Author: Aadil Ahamed
"""

class LiveConcert(object):
	
	def maxHappiness(self, h, s):
		table = {}
		for i  in range(len(s)):
			if s[i] in table:
				if h[i] > table[s[i]]:
					table[s[i]] = h[i]
			else:
				table[s[i]] = h[i]
		sum = 0
		for singer in table:
			sum += table[singer]
		return sum
		
		

def test_max_happiness():
	lc = LiveConcert()
	h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
	s = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a', 'abcde']
	ans = lc.maxHappiness(h, s)
	print(ans)
	

def main():
	test_max_happiness()
	
if __name__ == '__main__':
	main()
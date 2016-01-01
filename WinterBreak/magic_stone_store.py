import pdb

class MagicStoneStore(object):
	
	@staticmethod
	def generate_primes(n):
		"""
		Generate all prime numbers in [1, n]
		Returns a list of length n+1 where list[i] returns True if i is prime. Otherwise
		it returns False.
		"""
		is_prime = []
		for i in range(n+1):
			is_prime.append(True)
		is_prime[0] = False
		is_prime[1] = False
		for i in range(2, int(n ** (0.5)) + 1):
			if is_prime[i]:
				j = 2
				while(i*j <= n):
					is_prime[i*j] = False
					j += 1
		return is_prime
	
	def ableToDivide(self, n):
		is_prime = MagicStoneStore.generate_primes(2*n)
		for i in range(2, n+1):
			if is_prime[i]:
				if is_prime[2*n - i]:
					return 'YES'
		return 'NO'
		

def test_gen_primes():
	is_prime = MagicStoneStore.generate_primes(50)
	for i in range(len(is_prime)):
		print("i: {} is_prime: {}".format(i, is_prime[i]))
		
def test_able_to_divide():
	ms = MagicStoneStore()
	n = 1
	print('n = {}  ableToDivide = {}'.format(n, ms.ableToDivide(n)))
	n = 2
	print('n = {}  ableToDivide = {}'.format(n, ms.ableToDivide(n)))
	n = 3
	print('n = {}  ableToDivide = {}'.format(n, ms.ableToDivide(n)))
	n = 5
	print('n = {}  ableToDivide = {}'.format(n, ms.ableToDivide(n)))
	
	
def main():
	# test_gen_primes()
	test_able_to_divide()
	
if __name__ == '__main__':
	main()
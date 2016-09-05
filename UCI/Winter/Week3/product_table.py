"""
Author: Aadil Ahamed
Date: 1/23/15
Description: Python program to generate all possible combinations of products given a list of integers
"""


table = {}
def recursive_for(start, end, input_list):
	res = []
	if start in table:
		return table[start]
	elem = input_list[start]
	for i in range(start+1, end):
		int_res = recursive_for(i, end, input_list)
		for int_list in int_res:
			tmp = list(int_list)
			tmp.append(elem)
			res.append(tmp)
	res.append([elem])
	table[start]=res
	return res


def print_table(table):
	num = 1
	for key in table:
		for array in table[key]:
			out = str(num) + '.\t'
			res = array[0]
			for i in range(len(array)-1, 0, -1):
				out += str(array[i]) + '*'
				res *= array[i]
			out += str(array[0]) + ' = ' + str(res)
			print(out)
			num += 1
			
def product_table(input_list):
	recursive_for(0, len(input_list), input_list)
	print_table(table)
	
def test_rfor():
	list = ['a', 'b', 'c', 'd']
	recursive_for(0,len(list), list)
	print_table(table)
	
	
def main():
	ilist = [2, 3, 5, 7]
	# product_table(ilist)
	ilist = [2, 3, 5, 7, 9, 10]
	product_table(ilist)
	
if __name__ == '__main__':
	main()
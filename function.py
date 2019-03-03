def sum(number):
	result = 0
	for i in range(number+1):
		result = result + i
	return result

print(sum(6))
print(sum(10))

def largest(list):
	top = list[0]
	for value in list:
		if value > top:
			top = value
	return top

print(largest([10, 4, 2, 241, 91, 54]))
print(largest([1, 2, 3, 4, 0]))

def occurances(words, letters):
	return words.count(letters)

print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

def product(*args):
	product = 1
	for num in args:
		product *= num
	return product

print(product(6, 18, 1, 1, 1))
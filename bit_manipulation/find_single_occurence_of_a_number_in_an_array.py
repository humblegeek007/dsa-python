#Find the element that appears once in an array where every other element appears twice

input_array = [int(item) for item in input().split()]
res = input_array[0]
for i in range(1,len(input_array)):
	res = res ^ input_array[i]
print('the single occrence number is {}'.format(res))

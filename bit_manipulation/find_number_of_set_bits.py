x = int(input())
count = 0
while(x):
  x = x & (x-1)
  count = count + 1
print('the number of 1s in the number is : {}'.format(count))


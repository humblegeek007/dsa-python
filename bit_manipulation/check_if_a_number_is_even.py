# if the least bit is 0, this can be done by using the bit-wise AND

x = int(input())
if (x & 1 ) == 0:
  print('{} is even'.format(x))
else:
    print('{} is odd'.format(x))


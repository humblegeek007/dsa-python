# a number that is a power of two, should only have one 1 set;
# if we subtract 1, all the zeros following will be set to one. If we & that with the original number we get 0

x = int(input())

if (x & x-1) == 0:
  print('{} is power of 2'.format(x))
else:
    print('{} is not a power of 2'.format(x))


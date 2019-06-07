#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     07/07/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a, b = input().split()
a = int(a)
b = int(b)

if a + b == 15:
    print('+')
elif a * b == 15:
    print('*')
else:
    print('x')
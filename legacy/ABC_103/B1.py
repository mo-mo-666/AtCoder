#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     21/07/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a = list(input())
b = list(input())
i = 0
while True:
    c = b[-1]
    b = b[:-1]
    b = [c] + b
    if a == b:
        yesno = 'Yes'
        break
    i += 1
    if i > len(a)+1:
        yesno = 'No'
        break

print(yesno)
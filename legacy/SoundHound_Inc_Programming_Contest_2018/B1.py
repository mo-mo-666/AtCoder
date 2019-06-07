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




S = list(input())
w = int(input())
li = [S[w*i] for i in range(len(S)//w + 1)]
result = ''.join(li)

print(result)
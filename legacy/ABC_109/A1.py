#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     08/09/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a, b = map(int, input().split())

if a==2 or b==2:
    ans = 'No'
else:
    ans = 'Yes'

print(ans)
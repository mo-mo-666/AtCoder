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

n = int(input())

say = []
word = input()
say.append(word)
ans = 'Yes'

for i in range(n-1):
    word = input()
    if word in say:
        ans = 'No'

    elif word[0] != say[-1][-1]:
        ans = 'No'

    else:
        say.append(word)

print(ans)
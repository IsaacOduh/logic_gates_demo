# Author: Isaac
# Purpose: AI Class Code Task
# Date/Time: 22/12/17 - 3:30am
# This program is supposed to demo an xor relationship

x = int(input('Enter input X: '))
y = int(input('Enter input Y: '))

# I did a simple straight forward model (Long time since i wrote python code so forgive my ugly code ).
# I didnt factor in any user irregularities
# Please recall that XOR (exlusive Requires that only one must be 1 for it to output a true value)

if (x == 0 and y == 1) or (x == 1 and y == 0):
    output = 1
    print ('Value == ', + output)
else:
    output = 0
    print ('Value == ', + output)







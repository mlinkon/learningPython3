#Given an integer,n , print the following values for each integer from to
#    Decimal
#    Octal
#    Hexadecimal (capitalized)
#    Binary
#
#The four values must be printed on a single line in the order specified above for each
#from to . Each value should be space-padded to match the width of the binary value of
##
#Input Format
#
#A single integer denoting
#Output Format
#
#Print lines where each line (in the range ) contains the respective decimal, octal, capitalized hexadecimal, and binary values of n. 
#Each printed value must be formatted to the width of the binary value of n. 
#
#Constraints 1<= n<=100
##
# Code to work with python3.7
number = 17

length = len(bin(number).replace("0b", ""))

for f in range(1,number+1):
    binaryNumber = bin(f).replace("0b", "")
    octalNumber= oct(f).replace("0o", "")
    hexadecimal = hex(f).upper().replace("0X", "")
    print(f'{f:>{length}} {octalNumber:>{length}} {binaryNumber:>{length}} {hexadecimal:>{length}}')


n = int(input())
width = len("{0:b}".format(n))
for i in range(1,n+1):
    print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

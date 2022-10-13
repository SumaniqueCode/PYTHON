# Created on 2022/10/09
# By Suman Regmi

# Operators in Python
# This include Relational Operators, Logical Operators, bitwise Operators and Shorcut Operators.

# Relation Operators in Python:
#    <   >   <=    >=   ==   !=
a = 10
b = 20
c = 30
print("\nRelational Operator")
print(a > b)  # output will be false
print(a < c)  # output will be true
print(b != c, "\n")  # output will be true

# Logical Operators in Python:
# Logical AND
print("Logical AND")
# and operator gives true output if only both conditions are true.
print(a < c and b < c)
# here both conditions doesnot match so output will be false
print(c > b and a == b, "\n")

# Logical OR
print("Logical OR")
# or operator gives true output even if any one condition is true.
print(a < b or c < b, "\n")

# Logical NOT
# not(true)= false          not(false)= true
print("Logical NOT")
# a>b produces false output here but not of a>b produces true output.
print(not (a > b), "\n")

# Bitwise operator: (The output will always be in either 0 or 1)
# Bitwise AND operator ( & ): only 1 and 1 produces 1 remaining all produces are 0.
print("Bitwise AND operator")
# a = 10 = 1010    c = 30 = 11110   Output will be 1010 = 10.
print(a & c)
print(a & b, "\n")  # b = 20 = 10100    Output will be 0.

# Bitwise OR operator ( | ): only 0 and 0 produces 0 remaining all produces are 1.
print("Bitwise OR operator")
print(a | b)          # output will be 11110 = 30.
print(a | c, "\n")     # output will be 11110 = 30.

# Bitwise XOR operator ( ^ ): 0 and 0, 1 and 1 produces 0, remaining all produces 1.
print("Bitwise XOR operator")
print(a ^ b)          # output will be 11110 = 30.
print(b ^ c, "\n")     # output will be 1010 = 10

# Left shift
print("Left Shift")
print(a << 2, "\n")   # a*2*2 = 40

# Right shift
print("Right shift")
print(b >> 2, "\n")       # b/2*2 = 5

# Shortcut Operators in Python:
# +=    -=      *=      /=      //=     **=
print("Shortcut Operators")
a += b  # it means a = a+b = 30
print(a)
a *= b  # a = a*b = 600
print(a, "\n")

#BitPlay

a = 56
b = 12

#PART-1
print("---Bit Play 1---")
print("Before a : ",a,"Before b : ",b)
a = a+b
b = a-b
a = a - b
print('Swapped a : ',a,"Swapped b : ",b)
print()

#PART - 2
a = 56
b = 12
a = a ^ b
b = a ^ b
a = a ^ b
print('Swapped a : ',a,"Swapped b : ",b)
print()

# PART- 3
print("left shift")
print(" 3 << 1 = ", 3 << 1)
print(" 3 << 2 = ", 3 << 2)
print(" 3 << 3 = ", 3 << 3)
print(" 3 << 4 = ", 3 << 4)
print(" 3 << 5 = ", 3 << 5)
print()

# PART - 4
def divide( a,b) :
    negative = (a < 0) ^ (b < 0)
    a = abs(a)
    b = abs(b)
    count = 0
    while a>=b :
        a = a-b
        count = count+1
    if negative :
        count = -count
    return count

print ("Divide without :/")
print (" 50/ 2 =",divide(50,2))
print (" 72/ 3 =",divide(72,3))
print (" -50/ 2 =",divide(-50,2))
print (" 50/-2 =",divide(50,-2))


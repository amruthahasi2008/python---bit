a,b = 7,7
#Part 1
print("--- odd hunter---")
print("a^a",a ^ a)
print("a^0",a^0)
print("equal xor",(a ^ b)== 0)
print()

# part 2
arr = [3,5,3,5,9]
result = 0
for n in arr : result ^= n
print("XOR of ", arr ,"=",result)
print()

# part 3
nums = [4,7,4,2,7,2,9]
res = 0
for n in nums :
    res ^= n
print("pdd occuring num ", res)
print()

# part 4
pair = [3,9,3,5,5,7]
xab = 0
for n in pair : xab ^= n 
print("XOR  of two odds",xab ,"->", bin(xab))
print()

# part 5
setbit = xab & -xab
x,y = 0,0
for n in pair :
    if n & setbit :
        x ^= n
    else :
        y ^= n
print("two odd occuring numbers", x,"and", y)



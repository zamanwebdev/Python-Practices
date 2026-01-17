# Binary Type Data (bytes)
HabluList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,255]
A = bytes(HabluList)
print(type(A))
print(A[0])
# Binary Type Data (bytearray)
bytearrayList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,255]
b = bytearray(bytearrayList)
print(type(b))
print(b[0])
b[0] = 2
print(b[0])

#data type conversion
a = str(100)
b = int(a)
c = type(b)
print(c)

#same as
print(type(int(str(100))))
#list out the index
for i,char in enumerate('Helllooo'):
    print(i,char)

for i,char in enumerate([1,2,3]): #tuple be used too
    print(i,char)

for i,char in enumerate(list(range(100))):
  print(i,char)
  if char ==50:
     print(f'index of 50 is: {i}')
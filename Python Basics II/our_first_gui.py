#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

fill = '*'
empty = ' '
for row in picture:
    for pixel in row:
        if pixel == 1:
            print(fill, end='')
        else:
          print(empty, end= '')
    print('')

# 1 iterate over the picture
#if 0 -> print ''
#if 1 -> print *
#python doesnt necessarily need brackets for if statements
#make sure code i s clean, and readable, add comments in someplaces, so others can understand
#make it  a bit predictable
#DRY(do not repeat yourself), to reduce the line of code, make code reduceable
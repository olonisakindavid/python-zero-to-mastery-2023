#becareful with a while loop due to infite run time.. therefore the use of break or make sure the conditions ends
i = 0
while i < 50:
    print(i)
    # i = i+1
    i+= 1
    #break  ...no need to use this now
else:
    print('done')
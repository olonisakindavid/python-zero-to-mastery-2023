basket  = [1,2,3,4,5]
# adding method

basket.append(100)


basket.insert(4, 100)
basket.extend([101,100])


new_list = basket
print(new_list)
print(basket)


#removing
basket.pop() #pops the last thing and returns it
new_list = basket.pop(0) #we give it the index we want to remove, 
print(new_list) #returns a value 

new_list_2 = basket.remove(4) # we give it the number to remove... 
print(new_list_2)
print(basket)

clear = basket.clear()
print(basket)

amazon_cart = ['notebooks', 
               'sunglasses',
               'toys',
               'grapes'
               ]

# print(amazon_cart[0::2])

#unlike strings which are immutable, lists are immutable
# amazon_cart[0] = 'laptop'
# print(amazon_cart[1:3])
# print(amazon_cart)

amazon_cart[0] = 'laptop'
new_cart = amazon_cart
new_cart[0] ='gum'
print(new_cart)
print(amazon_cart)

#to copy to list actually use it next time
new_cart = amazon_cart[:]

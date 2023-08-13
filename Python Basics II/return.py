def sum_numbers(num1, num2):
    return num1 + num2

print(sum_numbers(2,3))

#a function should return something and also do one thing really well  --just a good practice .... the name must tally with its function

def sum_num(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)  #exits the function

total = sum_num(10,20)
print(total)
        

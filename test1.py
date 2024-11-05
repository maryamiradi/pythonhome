# number = 10
# assert number == 5 , ' this is invalid'
# print('number is 5')


li = []
def add_number(x):
    assert x not in li , 'soryy..'
    li.append(x)
add_number(2)
add_number(3)
add_number(1)
add_number(8)
print(li)


course= {'name':'python','price':250}
def add_discount(product,discount):
    price=product['price']- discount
    assert 0<=price<=product['price'] , ' dixcount is off'
    return price
print(add_discount(course,50))


    


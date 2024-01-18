even_squares = []
for e in range(8):
    if e%2==0:
        even_squares.append(e**2)
print(even_squares)

a = [1,2,3,'a','b', 'c', 1.2, 2.5]
b = [thing for thing in a if type(thing) == int]
print(b) 
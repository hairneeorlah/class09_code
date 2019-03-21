Answer = input('what side are u solving for?:\nhypotenuse?\nadjacent?\nopposite?')
if  Answer == 'opposite':
    a = float(input('enter the length of adjacent:'))
    c = float(input('enter the length of the hypotenuse:'))
    b_squared = (c**2) - (a**2)
    b = b_squared**0.5
    print('the length of the opposite side is:', b)
elif Answer == 'adjacent':
    b = float(input('enter the length of opposite:'))
    c = float(input('enter the length of the hypotenuse:'))
    a_squared = (c**2) - (b**2)
    a = a_squared**0.5
    print('the length of the adjacent side is:', a)
elif Answer == 'hypotenuse':
    b = float(input('enter the length of opposite:'))
    a = float(input('enter the length of the adjacent:'))
    c_squared = (a**2) + (b**2)
    c = c_squared**0.5
    print('the length of the hypotenuse is:', c)

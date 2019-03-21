# name = input('enter your name')
# if 'a' in name:
#     print('there exist a vovel in your name')
#     print('wow!')
#     print('names with the vowel A are beautiful')
# else:
#     print('there is no vowel A in your name')
boys_age = int(input('pls how old are you'))
boys_gratitude = 'merci'
list_of_gratitudes = ('ese','thanks', 'daalu', 'nagode', 'merci')

if boys_age >= 21:
    print('you are of the right age')
    payment = boys_age *100
    future_payment = 50 - boys_age
    print('take', str(payment) + 'USD')
    print('pls spend your money wisely')
    print('pls comeback in' , str(future_payment) , 'years', 'to collect 50000USD')

    if boys_gratitude in list_of_gratitudes:
        print('You are a good child')
        if payment >=3000:
            print('you are a big boy now')
        else:
            print('you are getting there')
else:
    print('your time is coming')



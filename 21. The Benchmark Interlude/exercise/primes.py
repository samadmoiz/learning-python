def prime(y):
    if y <= 1:
        print(y, 'is not prime')
    else:
        x = y // 2
        while x > 1:
            if y % x == 0:
                print(y, 'has factor', x)
                break
            x -= 1
        else:
            print(y, 'is prime')


prime(13)
prime(13.0)
prime(15)
prime(15.0)

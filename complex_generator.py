def complex_generator():
    print('Hey I just met you')

    items = [1, 2, 3]

    for item in items:
        print('And this is crazy')

        wtf = yield item

        print(wtf)

    print('But here is my number.')
    print('So call me maybe.')

    return 42

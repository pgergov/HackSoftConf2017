from simple_generator import simple_generator
from complex_generator import complex_generator


def another_generator():
    print('I like to do logic.')
    simple_gen = simple_generator()

    yield from simple_gen

    complex_gen = complex_generator()

    wtf = yield from complex_gen

    print(wtf)
    print('And I do it well.')

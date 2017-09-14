def is_prime(n):
    if n <= 1:
        return False

    counter = 2

    while counter < n:
        if n % counter == 0:
            return False

        counter += 1

    return True


def next_prime():
    counter = 1

    while True:
        if is_prime(counter):
            yield counter

        counter += 1

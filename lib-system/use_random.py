import random

if __name__ == '__main__':
    a = random.random()
    print(a)

    print(random.randint(1, 10))
    print(random.choice('tomorrow'))
    print(random.randrange(0, 100, 2))

    b = [1, 2, 3, 4, 5, 6]
    random.shuffle(b)
    print(b)

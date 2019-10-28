# 装饰器


def say_name(func):
    def inner():
        print("I'm Hardy")
        return func()
    return inner

@say_name
def say_hi():
    print('Hello, World')


if __name__ == '__main__':
    say_hi()

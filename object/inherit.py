class Animal(object):
    def run(self):
        print('Animal is running...')

    def run_twice(self):
        self.run()
        self.run()

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self, thing):
        print('Dog is Eating %s' % thing)

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
cat = Cat()

dog.run()
dog.run_twice()
dog.eat('meat')
cat.run()
cat.run_twice()
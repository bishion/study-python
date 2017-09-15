class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s : %s" % (self.__name, self.__score))

    def get_name(self):
        return self.__name


bart = Student("Guo", 100)
print(bart)
print(bart._Student__name)


# print(bart.__name)  # error


class Animal(object):
    def run(self):
        print("Animal is running...")


class Dog(Animal):
    def run(self):
        print("Dog is running")


class Cat(Animal):
    pass


dog = Dog()
dog.run()


print(type(dog))
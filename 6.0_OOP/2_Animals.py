'''2. Создайте класс «Animal» с тремя атрибутами и двумя методами. Создайте подклассы « Elefant», «Dog», «Cat»
с дополнительными атрибутами и методами (свойственными каждому животному). Выведите информацию о них на экран.'''


class Animal:
    def __init__(self, family, life_expectancy, nutrition):
        self.__family = family
        self.__nutrition = nutrition
        self.__life_expectancy = life_expectancy
        self.attrib = {'Семейство': self.__family,
                       'Цепь питания': self.__nutrition,
                       'Средння продолжительность жизни': self.__life_expectancy}

    @property
    def family(self):
        return self.__family

    @property
    def all_attrib(self):
        return self.attrib


class Elefant(Animal):
    def __init__(self, family, life_expectancy, nutrition):
        super().__init__(family, life_expectancy, nutrition)
        self.attrib['Отличительная особенность'] = 'Есть хобот.'


class Dog(Animal):
    def __init__(self, family, life_expectancy, nutrition):
        super().__init__(family, life_expectancy, nutrition)
        self.attrib['Отличительная особенноть'] = 'Лучший друг человек.'


class Cat(Animal):
    def __init__(self, family, life_expectancy, nutrition):
        super().__init__(family, life_expectancy, nutrition)
        self.attrib['Отличительная особенноть'] = "\'Имеет 9 жизней\'"
        self.preferences = None
        self.lives_count = 9

    def lifes_count(self):
        print(f'Осталось жизней: {self.lives_count}')

    def life_lost(self):
        self.lives_count = self.lives_count - 1


cat = Cat('Кошачьи', 10, 'Домашнее животное. Хищник.')
print(cat.all_attrib)
cat.lifes_count()
cat.life_lost()
cat.lifes_count()

elephant = Elefant('Слоновые', 60, 'Травоядные')
print(elephant.all_attrib)

dog = Dog('Псовые', 15, 'Домашние животные. Хищник')
print(dog.all_attrib)

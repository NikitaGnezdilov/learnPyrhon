# def name (a, b):
#     return a + b
# import math

# def is_even(n):
#     if n % 2 == 0:
#         print("True")
#     else:
#         print("False")
# is_even(n = int(input("Enter a number: ")))

# def say_hello(name):
#     print(f"Hello, {name}")
# say_hello("Tom")
# say_hello("Bob")
# say_hello("Alice")

# Округление до близайшего четного
# print(round(2.5))
# print(round(3.5))

# Написать lambda-функцию, принимающую 1 аргумент — сторону квадрата, и возвращающую периметр квадрата.
# print((lambda side: 4 * side)(5))

# Написать lambda-функцию, которая выводит среднее арифметическое 3 чисел.
# print((lambda  a, b, c: round(a+b+c)/++3)(1, 2 ,3))

# Прототип авторизации
# def main():
#     action = input("Registration or login? Enter: ")
#     def registration():
#         userName = input("Enter your name: ")
#         userSurname = input("Enter your surname: ")
#         userPassword = input("Enter your password: ")
#         userPasswordAgain = input("Enter your password again: ")
#
#         if userPassword == userPasswordAgain:
#             print("Welcome " + userName + "!")
#         else:
#             print("Sorry " + userName + "'s password does not match.")
#
#     def authorizationUser ():
#         userName_aut = input("Enter your name: ")
#         userSurname_aut = input("Enter your surname: ")
#         userPassword_aut = input("Enter your password: ")
#         userName_saved = "Nikita"
#         userSurname_saved = "Gnezdilov"
#         userPassword_saved = "123"
#
#         if userName_aut == userName_saved and userSurname_aut == userSurname_saved and userPassword_aut == userPassword_saved:
#             print("Welcome " + userName_saved)
#         else:
#             print("You entered an incorrect first or last name or password. Sorry " + userName_aut)
#     if action == "Registration" or action == "registration":
#         registration()
#     elif action == "login" or action == "Login":
#         authorizationUser()
#     else:
#         print("Sorry " + action + " is not a valid action. You need enter registration or login.")
#
# def question():
#     ans = input("If you want to continue working on our website, please log in or authorize. (Y/N): ")
#     if ans == "Y" or ans == "y":
#         main()
#     else:
#         print("Thank you! See you later")
# question()

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# elements = list(set(a) & set(b))
# print(elements)

# class Person:
# def __init__(self, name, age):
# self.name = name
# self.age = age


# tim = Person('Tim', 25)
# print(tim.name)
# print(tim.age)


# class Student:
# #     def __init__(self, name, age, city, height):
# #         self.name = name
# #         self.age = age
# #         self.city = city
# #         self.height = height
# #
# #
# # tom = Student('Tom', 19, city='San Francisco', height=180)
# # bob = Student('Bob', 21, city='Moscow', height=175)
# # allen = Student('Allen', 18, city='London', height=190)
# # # print("Name: " + tom.name + ", Age: " + str(tom.age) + ", City: " + tom.city + ", Height: " + str(tom.height))
# # # print("Name: " + bob.name + ", Age: " + str(bob.age) + ", City: " + bob.city + ", Height: " + str(bob.height))
# # # print("Name: " + allen.name + ", Age: " + str(allen.age) + ", City: " + allen.city + ", Height: " + str(allen.height))
# # print(f"Name: {tom.name}, Age: {tom.age}, City: {tom.city}, Height: {tom.height}")
# # print(f"Name: {bob.name}, Age: {bob.age}, City: {bob.city}, Height: {bob.height}")
# # print(f"Name: {allen.name}, Age: {allen.age}, City: {allen.city}, Height: {allen.height}")

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
#     def circumference(self):
#         return 2 * math.pi * self.radius
#
#
# circle = Circle(2)
# print(circle.area())
# print(circle.circumference())

# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # устанавливаем имя
#         self.__age = age  # устанавливаем возраст
#
#     def print_person(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
#
#
# tom = Person("Tom", 39)
# tom.__name = "Человек-паук"  # пытаемся изменить атрибут __name
# tom.__age = -129  # пытаемся изменить атрибут __
# # tom.print_person()  # Имя: Tom        Возраст: 39


# class House:
#     def __init__(self, number, age, street, house_type):
#         self.number = number
#         self.age = age
#         self.street = street
#         self.house_type = house_type
#
#     def print_house(self):
#         print(
#             f"Номер дома: {self.number}, улица дома: {self.street}, возраст дома: {self.age}, тип дома: {self.house_type}.")
#
#
# firstHouse = House(1, 10, "Pushkina", "multi-storey")
# secondHouse = House(2, 13, "Pushkina", "multi-storey")
# thirdHouse = House(3, 12, "Pushkina", "multi-storey")
# fourthHouse = House(4, 11, "Pushkina", "multi-storey")
# firstHouse.print_house()
# secondHouse.print_house()
# thirdHouse.print_house()
# fourthHouse.print_house()
# """Данные больницы"""
#
#
# class Hospital:
#     """Инициализирует имя, адрес, город и состояние посетителя."""
#
#     def __init__(self, name, age, address, city, state):
#         self.__name = name
#         self.__age = age
#         self.__address = address
#         self.__city = city
#         self.__state = state
#
#     """Выводит всю информацию в командную строку"""
#
#     def print_information(self):
#         print(
#             f"Name: {self.__name}, Age: {self.__age}, Address: {self.__address}, City: {self.__city}, State: {self.__state}")
#
#     """Сеттер для установления возраста"""
#
#     def set_age(self, age):
#         if 0 < age < 100:
#             self.__age = age
#         else:
#             print("Incorrect Age")
#
#     """Сеттер для установления адреса"""
#
#     def set_address(self, address_string):
#         self.__address = address_string
#
#     """Сеттер для установления города проживания"""
#
#     def set_city(self, city_string):
#         self.__city = city_string
#
#     """Сеттер для установления состояния посетителя"""
#
#     def set_state(self, state_string):
#         self.__state = state_string
#
#     """Геттер для получения установленного возраста"""
#
#     def get_age(self):
#         return self.__age
#
#     """Геттер для получения установленного адреса"""
#
#     def get_address(self):
#         return self.__address
#
#     """Геттер для получения установленного города проживания посетителя больницы"""
#
#     def get_city(self):
#         return self.__city
#
#     """Геттер для получения установленного состояние посетителя больницы"""
#
#     def get_state(self):
#         return self.__state
#
#
# tom = Hospital("Tom", 15, "Pushkina 4", "Moscow", "Sick")
# tom.set_age(25)
# tom.set_state("A little sick")
# tom.set_city("Tombow")
# tom.print_information()

# class Hospital:
#     """Инициализирует имя, адрес, город и состояние посетителя."""
#
#     def __init__(self, name, age, address, city, state):
#         self.__name = name
#         self.__age = age
#         self.__address = address
#         self.__city = city
#         self.__state = state
#
#     """Выводит всю информацию в командную строку"""
#
#     def print_information(self):
#         print(
#             f"Name: {self.__name}, Age: {self.__age}, Address: {self.__address}, City: {self.__city}, State: {self.__state}")
#
#     """Сеттер для установления возраста"""
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 0 < age < 100:
#             self.__age = age
#         else:
#             print("Incorrect Age")
#
#     """Сеттер для установления адреса"""
#
#     @property
#     def address(self):
#         return self.__address
#
#     @address.setter
#     def address(self, address_string):
#         self.__address = address_string
#
#     """Сеттер для установления города проживания"""
#
#     @property
#     def city(self):
#         return self.__city
#
#     @city.setter
#     def city(self, city_string):
#         self.__city = city_string
#
#     """Сеттер для установления состояния посетителя"""
#
#     @property
#     def state(self):
#         return self.__state
#
#     @state.setter
#     def state(self, state_string):
#         self.__state = state_string
#
#
# tom = Hospital("Tom", 15, "Pushkina 4", "Moscow", "Sick")
# tom.age = 25
# tom.state = "A little sick"
# tom.city = "Tombow"
# tom.print_information()

# class Person:
#     def __init__(self, name, age, city):
#         self.__name = name
#         self.__age = age
#         self.__city = city
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name_str):
#         self.__name = name_str
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age_str):
#         self.__age = age_str
#
#     @property
#     def city(self):
#         return self.__city
#
#     @city.setter
#     def city(self, city_str):
#         self.__city = city_str
#
#
# class Student(Person):
#
#     def student_info(self):
#         print(f"Name: {self.name}, age: {self.age}, city: {self.city}")
#
#
# tom = Student("Tom", 34, "Moscow")
# tom.student_info()

# class Person:
#     type = "Person"
#     description = "Describes a person"
#
#     def __init__(self, name):
#         self.__name = name
#
#     def print_name(self):
#         print(f"Hello {self.name}")
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#
# tom = Person("Tom")
# bob = Person("Bob")
# tim = Person("Tim")
# nick = Person("Nick")
# answer = str(input("What is your name? "))
#
# if answer == tom.name:
#     print(tom.type, "is you")
#     print(tom.description)
#     print(tom.name)
# elif answer == bob.name:
#     print(bob.type, "is you")
#     print(bob.description)
#     print(bob.name)
# elif answer == tim.name:
#     print(tim.type, "is you")
#     print(tim.description)
#     print(tim.name)
# elif answer == nick.name:
#     print(nick.type, "is you")
#     print(nick.description)
#     print(nick.name)
#     print(tom.name)
# else:
#     print("Incorrect name")


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return Number(self.value + other.value)
#
#     def __str__(self):
#         return f"{self.value}"
#
# num1 = Number(5)
# num2 = Number(6)
# sum = num1 + num2
# print(sum)

# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def __bool__(self):
#         return self.value > 0
#
# def num(Number):
#     if Number: print(f'Number true: {Number.value}')
#     else: print(f'Number false: {Number.value}')
#
# result1 = Number(1)
# num(result1)
#
# result2 = Number(-1)
# num(result2)

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def __getitem__(self, prop):
#         if prop == "name":
#             return self.__name
#         elif prop == "age":
#             return self.__age
#         return None
#
# p1 = Person("John", 25)
# print("Name: ", p1["name"])
# print("Age: ", p1["age"])

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def __contains__(self, prop):
#         if prop == 'name' or prop == 'age': return True
#         return False
#
# p1 = Person("John", 25)
# print("name" in p1)
# print("age" in p1)
# print("id  " in p1)

# def name (a, b):
#     return a + b
import math

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

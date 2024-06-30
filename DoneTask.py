# def name (a, b):
#     return a + b


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

action = input("Registration or login? Enter: ")
def registration():
    userName = input("Enter your name: ")
    userSurname = input("Enter your surname: ")
    userPassword = input("Enter your password: ")
    userPasswordAgain = input("Enter your password again: ")

    if userPassword == userPasswordAgain:
        print("Welcome " + userName + "!")
    else:
        print("Sorry " + userName + "'s password does not match.")

def authorizationUser ():
    userName_aut = input("Enter your name: ")
    userSurname_aut = input("Enter your surname: ")
    userPassword_aut = input("Enter your password: ")

    print("Welcome " + userName_aut)

if action == "Registration" or action == "registration":
    registration()
elif action == "login" or action == "Login":
    authorizationUser()
else:
    print("Sorry " + action + " is not a valid action. You need enter registration or login.")


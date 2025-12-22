#Задание 1
def greet(name):
    print(f"Привет, {name}")
name = str(input("Введите свое имя:"))
greet(name)

#Задание 2
def square(number):
    return number **2
number =int(input("Введите число:"))
print("Квадрат введенного числа:", square(number))

#Задание 3
def max_of_two(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        print("Числа равны")
x = int(input("Введите первое число:"))
y = int(input("Введите второе число:"))
print("Бошьшее число:", max_of_two(x, y))

#Задание 4
def describe_person(name, age=30):
    print(f"Имя: {name}, Возраст: {age}")
name = str(input("Введите имя:"))
a = str(input("Хотите ввести имя? (да/нет)"))
if a == "да":
    age = str(input("Введите возраст:"))
    describe_person(name, age)
else:
    describe_person(name)

age = input()

if age:
    print(describe_person(name, age))
else:
    print(describe_person(name))

#Задание 5
def is_prime(number):
    if number == 2 or number == 3 or number == 5 or number == 7:
        return True
    elif number == 1 or number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        return False
    else:
        return True

number = int(input("Введите число:"))
r = is_prime(number)
print(r)
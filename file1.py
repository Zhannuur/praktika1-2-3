# 1. Айнымалылар және мәліметтер типтері
name = "Aruzhan"
age = 19
gpa = 3.5
is_student = True

print(name)
print(age)
print(gpa)
print(is_student)


# 2. Шартты операторлар (if, else)
number = int(input("Сан енгізіңіз: "))
if number % 2 == 0:
    print("Жұп сан")
else:
    print("Тақ сан")


# 3.1 for циклі
for i in range(1, 6):
    print(i)

# 3.2 while циклі
i = 1
while i <= 5:
    print(i)
    i += 1


# 4.1 Калькулятор бағдарламасы
a = float(input("Бірінші сан: "))
b = float(input("Екінші сан: "))
operation = input("Операция (+, -, *, /): ")

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("Кате операция")


# 4.2 Жұп/тақ сан анықтау бағдарламасы
number = int(input("Сан енгізіңіз: "))
if number % 2 == 0:
    print("Жұп сан")
else:
    print("Тақ сан")

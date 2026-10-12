print ("Добро пожаловать в калькулятор! \n\nВведите первое число:")
first_number = float(input())

print ("Ваше первое число: " + str(first_number) + "\n\nВведите второе число:")
second_number = float(input())

print ("Ваше второе число: " + str(second_number) + "\n\nВыберите опператор:")
print ("Возможные опператоры: +,-, /, *")
operator = input()

if operator == "+":
    result = first_number + second_number
if operator == "-":
    result = first_number - second_number
if operator == "/":
    result = first_number / second_number
if operator == "*":
    result = first_number * second_number

print("Ваш результат: " + str(result))

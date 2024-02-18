# Запитуємо у користувача чотири числа
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Обчислюємо суми перших двох чисел та інших двох чисел
sum1 = num1 + num2
sum2 = num3 + num4

# Розділяємо першу суму на другу
result = sum1 / sum2

# Виводимо результат з двома цифрами після коми
print("Result:", "{:.2f}".format(result))
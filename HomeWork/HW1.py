# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input("Введите трёхзначное число: "))
result = n // 100 + n % 10 + n % 100 // 10
print(result)
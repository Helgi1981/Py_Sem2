# Задача №9. Решение в группах

# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# Input: 5
# Output: 120

n = 5
f = 1

while n > 1:
    f *= n
    n -= 1
print(f)

# Рекурсия:
def func(n, f = 1):
    if n == 1:
        return f
    return func(n - 1, f * n)

print(func(5))

# Команда делать что-то, если файл является запускаемой программой (строки 16 и 24)
# Эти строки можно запустить в другом файле, прописав в нём: "import Task1"
# Для этого нужно создать файл в текущем репозитории и прописать в нём эту команду
if __name__ == '__main__':
    print(func(5))

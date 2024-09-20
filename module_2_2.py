first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
# Если все числа равны между собой, то вывести 3
if first==second and second==third:
    print('Все',3,'числа равны')
# Если хотя бы 2 из 3 введенных чисел равны между собой, то вывести 2
elif first == second or first == third or second == third:
    print(2, 'из 3 равны')
# Если равных чисел среди 3-х вообще нет, то вывести 0
else:
    print(0, 'нет равных чисел')
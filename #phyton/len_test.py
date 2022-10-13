print('Вечер в хату! Введите первую строку:')
str1 = input()

print('Теперь вторую пёс!:')
str2 = input()

dl1 = len(str1)
dl2 = len(str2)

longer_length = max(dl1, dl2)
print(longer_length)
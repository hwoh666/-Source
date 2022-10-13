
print('Вечер в хату! Введите первую строку:')
s1 = input()

print('Теперь вторую пёс!:')
s2 = input()

print('Можешь вводить последнюю для тебя сладкий!:')
s3 = input()  

joined_with_commas = f'{s1}, {s2}, {s3}'
print(joined_with_commas)

joined_with_commas = f' {s1}\n {s2}\n {s3}'
print(joined_with_commas)

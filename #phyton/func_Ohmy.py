#здесь мы стартуем изучать функции

num = int(input('Вводи число какое вдумается псина, а я скажу то что ты и так знаешь:'))
# Сама ее виличество ебейшая функция.
def get_num_type(num):
    if num == 0: 
        print ("Очко !")
    elif num > 0:
        print ("Число больше нуля Пёс!")
    elif num < 0:
        print ("Число меньше нуля Пёс!")
    return
#Вот тут мы ее вызвали и она вернула значение Print.
get_num_type(num)
# Вот тут мы признали пользу написаного.
print("Ебать полезно!!!")
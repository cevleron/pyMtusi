# Во время путешествия с родителями в Болгарию Фёдор был удивлён тем,
# что стоимость напитка в магазине можно уменьшить, если вернуть пустую
# бутылку обратно в магазин. У Фёдора есть А рублей, бутылка с соком
# стоит В рублей, пустая бутылка стоит С рублей.
# Фёдор решил написать программу, которая вычисляет, сколько бутылок с
# соком он сможет выпить, если будет сдавать пустые бутылки и на вырученные
# деньги покупать полные. Полученная сдача добавляется к выручке.
# Формат ввода
# Вводится последовательно в трех разных строках три числа А, В, С Формат вывода
# Выведите одно число ? количество бутылок с соком.
#
# a - количество денег
# b - стоимость сока
# с - стоимость пустой бутылки

# a=int(input())
# b=int(input())
# c=int(input())
# s1 = (a - c) // (b - c)
# print(s1)

try:
    a = int(input())
    b = int(input())
    c = int(input())
    if a<=0 or b<= 0 or c<=0: exit('Упс что-то пошло не так')
    s1 = (a - c) // (b - c)
    print(s1)
except:
    print('Упс что-то пошло не так')
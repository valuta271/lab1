#Вариант 6
#Задание №1
#Цвета
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

#Флаг
print(RED,'                         ',END)
print(WHITE,'                         ',END)
print(BLUE,'                         ',END)
print(BLUE,'                         ',END)
print(WHITE,'                         ',END)
print(RED,'                         ',END)

#Задание№2
#Строим из блоков фигуру
pattern = [
          "         ██  ",
          "       ██  ██ ",
          "     ███    ███",
          "   ███        ███ ",
          " ███            ███",
]
#Красим и выводим
for line in pattern:
    colored = line.replace('█', f'{BLUE} {END}')
    print((colored + '  '))
#Задание №3
#не получилось :(




def iterate(array, cand, valuer=[], val_ar=[]):  # Перебор расписания
    watcher = cand
    valuer = valuer.copy()
    valuer.append(watcher[2])
    for i in range(len(array)):
        if watcher[1] <= array[i][0] and watcher[2] != array[i][2]:
            iterate(array, array[i], valuer, val_ar)
    val_ar.append(valuer)
    return val_ar


def optim(array, val_ar):  # Поиск оптимального варианта расписания
    top = 1
    for i in val_ar:  # Находим максимальное количество заявок
        if len(i) > top:
            top = len(i)
    new_time = []
    for i in val_ar:  # Находим выступления с наибольшим числом заявок
        if len(i) == top:
            new_time.append(i)
    val_ar = new_time
    best_time = 0  # Убираем более длинные заявки
    best = val_ar[0]
    for val in val_ar:
        duration = 0
        for el in val:
            dur = int(array[el - 1][1]) - int(array[el - 1][0])
            duration += dur
        if duration < best_time:
            best_time = duration
            best = val
    return best


with open('input.txt') as f:  # Открываем файл
    N = int(f.readline())
    timetable = []
    for i in range(N):
        timetable.append(f.readline().split())
    c = 0
    for element in timetable:  # Добавляем к расписанию порядковый номер
        c += 1
        element.append(c)
    new_array = []
    for i in range(len(timetable)):  # Запускаем функцию для каждого начального положения
        a = iterate(timetable, timetable[1])
        a = optim(timetable, a)
        if a not in new_array:
            new_array.append(a)
    new_array = new_array[0]
    string = ' '.join([str(i) for i in new_array])

with open('output.txt', 'w') as f:  # Вывод
    f.write(string)

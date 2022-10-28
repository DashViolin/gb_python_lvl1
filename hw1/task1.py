total_turns = int(input('Введите количество повторов: '))

for _ in range(total_turns):
    duration = int(input('Введидте продолжительность в секундах: '))
    if duration > 0:
        days = duration // 86400
        hours = (duration - days * 86400) // 3600
        mins = (duration - days * 86400 - hours * 3600) // 60
        secs = duration % 60
        result = ''
        if days:
            result += str(days) + ' дн '
        if hours:
            result += str(hours) + ' час '
        if mins:
            result += str(mins) + ' мин '
        if secs:
            result += str(secs) + ' сек'
        print(result)
    else:
        print('Число не должно быть меньше 0.')

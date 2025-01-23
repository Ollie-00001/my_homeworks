time = int(input("Введите время в секундах: "))
temperature = int(input("Введите температуру в градусах Цельсия: "))

def pluralize(n, singular, few, many):
    if 11 <= n % 100 <= 19:
        return many
    elif n % 10 == 1:
        return singular
    elif 2 <= n % 10 <= 4:
        return few
    else:
        return many

def convert_time(time):
    hours = time // 3600
    minutes = (time - hours * 3600) // 60
    seconds = time - hours * 3600 - minutes * 60
    return hours, minutes, seconds

def convert_temperature(temperature):
    fahrenheit = temperature * 9 / 5 + 32
    kelvin = temperature + 273.15
    reomur = temperature * 4 / 5
    return fahrenheit, kelvin, reomur

hours, minutes, seconds = convert_time(time)
fahrenheit, kelvin, reomur = convert_temperature(temperature)

print(
    f"Время: {hours} {pluralize(hours, 'час', 'часа', 'часов')}, "
    f"{minutes} {pluralize(minutes, 'минута', 'минуты', 'минут')}, "
    f"{seconds} {pluralize(seconds, 'секунда', 'секунды', 'секунд')}\n"
    f"Температура: {fahrenheit:.2f} {pluralize(int(fahrenheit), 'градус', 'градуса', 'градусов')} по Фаренгейту, "
    f"{kelvin:.2f} {pluralize(int(kelvin), 'градус', 'градуса', 'градусов')} по Кельвину, "
    f"{reomur:.2f} {pluralize(int(reomur), 'градус', 'градуса', 'градусов')} по Реомюру"
)

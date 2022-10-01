import json


dict = json.load(open('D:/A_Main/Python/Hillel/Hw_7/acdc.json', 'r', encoding='utf-8'))

mass_duration = []

# заповнюю масив тривалістю треків
for i in dict['album']['tracks']['track']:
    mass_duration.append(i['duration'])

# перетворюю масив чисел в int з str
mass_duration = [int(i) for i in mass_duration]

# знаходжу сумму у секундах
sum_duration = sum(mass_duration)


def convert(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return "%02d:%02d:%02d" % (hour, min, sec)

sec = sum_duration
print("Time: ", convert(sec))


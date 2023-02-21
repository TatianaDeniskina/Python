time_sec = int(input("Введите время в секундах:"))
hour = time_sec // 3600
time_sec = time_sec % 3600
minutes = time_sec // 60
seconds = time_sec % 60
print("Количество часов:", hour)
print("Количество минут:", minutes)
print("Количество секунд:", seconds)
print(hour, ":", minutes, ":", seconds)

# bornday.py

# Спросить у пользователя год рождения А.С. Пушкина
year = input("Введите год рождения А.С. Пушкина: ")

# Проверка года рождения
if year == "1799":
    # Если год введен верно, спросить день рождения
    day = input("Введите день рождения А.С. Пушкина: ")
    if day == "6 июня":
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год")
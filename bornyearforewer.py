correct_year = 1799 

while True:
    user_input = input("Введите год рождения: ")
    try:
        year = int(user_input)
        if year == correct_year:
            print("Верно")
            break
        else:
            print("Неверный год, попробуйте снова.")
    except ValueError:
        print("Пожалуйста, введите числовое значение.")
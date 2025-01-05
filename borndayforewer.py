correct_year = 1799
correct_date = "6 июня"

while True:
    user_input_year = input("Введите год рождения А.С. Пушкина: ")
    try:
        year = int(user_input_year)
        if year == correct_year:
            print("Год указан верно")
            while True:
                user_input_date = input("Введите день рождения А.С. Пушкина: ")
                date = str(user_input_date)
                if date == correct_date:
                    print("Верно")
                    exit()
                else:
                    print("Неверный день рождения, попробуйте снова.")
        else:
            print("Неверный год, попробуйте снова.")
    except ValueError:
        print("Пожалуйста, введите числовое значение.")

def quiz():
    # Список знаменитостей и их годов рождения
    celebrities = {
        "Albert Einstein": 1879,  # Правильный ответ: 1879
        "Isaac Newton": 1643,     # Правильный ответ: 1643
        "Leonardo da Vinci": 1452, # Правильный ответ: 1452
        "Galileo Galilei": 1564,  # Правильный ответ: 1564
        "Marie Curie": 1867       # Правильный ответ: 1867
    }

    correct_answers = 0
    total_questions = len(celebrities)

    for celebrity, birth_year in celebrities.items():
        try:
            answer = int(input(f"Введите год рождения {celebrity}: "))
            if answer == birth_year:
                correct_answers += 1
        except ValueError:
            print("Пожалуйста, введите числовое значение.")

    incorrect_answers = total_questions - correct_answers
    correct_percentage = (correct_answers * 100) / total_questions
    incorrect_percentage = (incorrect_answers * 100) / total_questions

    print(f"\nКоличество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {incorrect_answers}")
    print(f"Процент правильных ответов: {correct_percentage:.2f}%")
    print(f"Процент неправильных ответов: {incorrect_percentage:.2f}%")

    restart = input("\nХотите начать игру сначала? (да/нет): ").strip().lower()
    if restart == "да":
        quiz()
    else:
        print("Спасибо за игру!")

if __name__ == "__main__":
    quiz()
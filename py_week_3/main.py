student_name = input("Enter student's name: ")
student_mark = input("Enter student's mark: ")

levels = {
    '1': 'Начальный уровень',
    '2': 'Начальный уровень',
    '3': 'Начальный уровень',
    '4': 'Средний уровень',
    '5': 'Средний уровень',
    '6': 'Средний уровень',
    '7': 'Достаточный уровень',
    '8': 'Достаточный уровень',
    '9': 'Достаточный уровень',
    '10': 'Высокий уровень',
    '11': 'Высокий уровень',
    '12': 'Высокий уровень'
}

if student_mark.isdigit():
    student_mark = int(student_mark)
    
    if 1 <= student_mark <= 12:
        level = levels[str(student_mark)]
        print(f"Имя студента: {student_name}. Уровень: {level}.")
    else:
        print("Оценка должна быть от 1 до 12.")
else:
    print("Invalid input. Please enter a valid number.")
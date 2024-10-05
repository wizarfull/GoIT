def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                _, salary = line.strip().split(',')
                total += int(salary)
                count += 1
        average = total / count if count > 0 else 0
        return total, average
    except FileNotFoundError:
        print("Файл не знайдено")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

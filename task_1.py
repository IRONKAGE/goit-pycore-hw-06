def total_salary(path):
    total_sum = 0
    developer_count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary_str = line.strip().split(',')
                    salary = int(salary_str)
                    total_sum += salary
                    developer_count += 1
                except ValueError:
                    print(f"Помилка формату рядка: '{line.strip()}' - пропущено.")
                    continue
                except IndexError:
                    print(f"Помилка формату рядка: '{line.strip()}' - пропущено.")
                    continue

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return (0, 0)
    except IOError as e:
        print(f"Помилка вводу/виводу при роботі з файлом '{path}': {e}")
        return (0, 0)

    if developer_count > 0:
        average_salary = total_sum / developer_count
    else:
        average_salary = 0
        print("Файл порожній або не містить коректних даних.")

    return (total_sum, average_salary)

# Приклад використання
# Створення фіктивного файлу для демонстрації
try:
    with open("salary_file.txt", "w", encoding="utf-8") as f:
        f.write("Alex Korp,3000\n")
        f.write("Nikita Borisenko,2000\n")
        f.write("Sitarama Raju,1000\n")
        f.write("Invalid Line\n") # Рядок з помилкою формату
except IOError as e:
    print(f"Не вдалося створити тестовий файл: {e}")

# Використання функції зі справжнім файлом
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# Приклад використання з неіснуючим файлом
total_err, average_err = total_salary("non_existent_file.txt")
print(f"Загальна сума заробітної плати (помилка): {total_err}, Середня заробітна плата (помилка): {average_err}")

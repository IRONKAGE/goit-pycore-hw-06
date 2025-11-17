def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_list.append(cat_dict)
                except ValueError:
                    print(f"Помилка формату рядка: '{line.strip()}' - пропущено.")
                    continue
                except IndexError:
                    print(f"Помилка формату рядка: '{line.strip()}' - пропущено.")
                    continue

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return []
    except IOError as e:
        print(f"Помилка вводу/виводу при роботі з файлом '{path}': {e}")
        return []

    return cats_list

# Приклад використання
# Створення фіктивного файлу для тестування (якщо потрібно)
try:
    with open("cats_file.txt", "w", encoding="utf-8") as f:
        f.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
        f.write("60b90c2413067a15887e1ae2,Vika,1\n")
        f.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
        f.write("60b90c3b13067a15887e1ae4,Simon,12\n")
        f.write("60b90c4613067a15887e1ae5,Tessi,5\n")
        f.write("invalid_line\n") # Рядок з помилкою формату
except IOError as e:
    print(f"Не вдалося створити тестовий файл: {e}")

# Використання функції зі справжнім файлом
cats_info = get_cats_info("cats_file.txt")
print(cats_info)

# Приклад використання з неіснуючим файлом
cats_info_err = get_cats_info("non_existent_cats_file.txt")
print(f"Результат для неіснуючого файлу: {cats_info_err}")

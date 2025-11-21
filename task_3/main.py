# Козлова 1 вариант
import json
import os
print("start code ...")

filename = "fishes.json"

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        fishes = json.load(f)
else:
    fishes = []

operation_count = 0

while True:
    print("\nМеню выбора:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")
    
    choice = input("Выберите один из пунктов (1-5): ").strip()
    
    if choice == "1":
        print("\n============== Все записи ==============")
        if not fishes:
            print("Нет записей.")
        else:
            for fish in fishes:
                salt_water_str = "морская рыба" if fish["is_salt_water_fish"] else "пресноводная рыба"
                print(f"ID: {fish['id']}")
                print(f"Общее название: {fish['name']}")
                print(f"Латинское название: {fish['latin_name']}")
                print(f"Морская рыба: {salt_water_str}")
                print(f"Количество подвидов рыбы: {fish['sub_type_count']}")
                print("-" * 40)
        operation_count += 1

    elif choice == "2":
        try:
            target_id = int(input("Введите ID рыбы: "))
            found = False
            for index, fish in enumerate(fishes):
                if fish["id"] == target_id:
                    print(f"\n============== Найдено ==============")
                    print(f"Позиция в списке: {index + 1}")
                    salt_water_str = "морская рыба" if fish["is_salt_water_fish"] else "пресноводная рыба"
                    print(f"ID: {fish['id']}")
                    print(f"Общее название: {fish['name']}")
                    print(f"Латинское название: {fish['latin_name']}")
                    print(f"Морская рыба: {salt_water_str}")
                    print(f"Количество подвидов рыбы: {fish['sub_type_count']}")
                    found = True
                    break
            if not found:
                print("\n============== Не найдено ===============")
        except ValueError:
            print("Некорректный ввод ID.")
        operation_count += 1

    elif choice == "3":
        try:
            new_id = max([s["id"] for s in fishes], default=0) + 1
            name = input("Введите общее название рыбы: ").strip()
            latin_name = input("Введите научное название рыбы: ").strip()
            is_salt_water_input = input("Это морская рыба? (да/нет): ").strip().lower()
            is_salt_water_fish = True if is_salt_water_input in ("да", "yes", "y", "1") else False
            sub_type_count = float(input("Введите количество подвидов рыбы: "))
            new_fish = {
                "id": new_id,
                "name": name,
                "latin_name": latin_name,
                "is_salt_water_fish": is_salt_water_fish,
                "sub_type_count": sub_type_count
            }
            fishes.append(new_fish)
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(fishes, f, ensure_ascii=False, indent=4)
            print("Запись успешно добавлена.")
        except ValueError:
            print("Ошибка: количество подвидов должно быть числом.")
        operation_count += 1

    elif choice == "4":
        try:
            target_id = int(input("Введите ID рыбы для удаления: "))
            initial_len = len(fishes)
            fishes = [s for s in fishes if s["id"] != target_id]
            if len(fishes) == initial_len:
                print("\n============== Не найдено ===============")
            else:
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(fishes, f, ensure_ascii=False, indent=4)
                print("Запись успешно удалена.")
        except ValueError:
            print("Некорректный ввод ID.")
        operation_count += 1

    elif choice == "5":
        print(f"\nВыполнено операций: {operation_count}")
        print("... end code")
        break

    else:
        print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")

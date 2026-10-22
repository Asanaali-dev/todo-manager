import json
FILENAME = "tasks.json"
def load_tasks():
    """Читает задачи из файла. Если файла нет, возвращает пустой список."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Записывает задачи в файл."""
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

def show_tasks(tasks):
    print("\nВаши задачи:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- СПИСОК ЗАДАЧ ---")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выход")

        choice = input("\nВыберите пункт (1-4): ")

        if choice == "1":
            if not tasks:
                print("\nСписок пуст!")
            else:
                show_tasks(tasks)

        elif choice == "2":
            new_task = input("\nВведите новую задачу: ").strip()
            if new_task != "":
                tasks.append(new_task)
                save_tasks(tasks)
                print(f"Задача '{new_task}' добавлена!")
            else:
                print("Задача не может быть пустой!")

        elif choice == "3":
            if not tasks:
                print("\nНечего удалять, список пуст.")
            else:
                show_tasks(tasks)
                num_str = input("\nВведите номер задачи для удаления: ")

                if num_str.isdigit():
                    num = int(num_str)
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_tasks(tasks)
                        print(f"Задача '{removed}' удалена!")
                    else:
                        print("Нет задачи с таким номером!")
                else:
                    print("Пожалуйста, введите число!")

        elif choice == "4":
            print("\nПрограмма завершена. Пока!")
            break

        else:
            print("\nНеверный выбор! Введите число от 1 до 4.")

if __name__ == "__main__":
    main()
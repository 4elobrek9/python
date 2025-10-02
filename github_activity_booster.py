import os
import subprocess
import random
import string
import datetime
import time

# --- НАСТРОЙКИ ---
# Общее количество коммитов, которое будет выполнено
NUM_COMMITS = 15 
# Количество строк для генерации в ОДНОМ файле. 500,000 строк обеспечит максимальный вклад.
NUM_LINES_TO_GENERATE = 500000 
# Имя папки, куда будут записываться сгенерированные файлы.
CACHE_DIR = "cache" 

# --- ФУНКЦИИ ГЕНЕРАЦИИ ---

def get_unique_filename():
    """Генерирует уникальное имя файла в папке кэша и создает папку, если ее нет."""
    # Создаем папку, если ее еще нет
    os.makedirs(CACHE_DIR, exist_ok=True)
    
    # Формируем путь к файлу
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(CACHE_DIR, f"activity_data_{timestamp}.txt")

def generate_large_content(num_lines: int) -> str:
    """Генерирует большой объем случайного строкового контента."""
    print(f"-> Начинается генерация {num_lines} случайных строк...")
    content_list = []
    
    # Случайный набор символов для строк (буквы, цифры, знаки препинания и много пробелов)
    chars = string.ascii_letters + string.digits + string.punctuation + ' ' * 10
    
    for _ in range(num_lines):
        # Генерируем строку случайной длины (от 50 до 150 символов)
        line_length = random.randint(50, 150)
        random_line = ''.join(random.choice(chars) for _ in range(line_length))
        content_list.append(random_line)
    
    print("-> Генерация завершена.")
    # Объединяем строки, добавляя в конце символ новой строки (\n)
    return "\n".join(content_list)

def generate_random_commit_message(filename: str, num_lines: int, iteration: int) -> str:
    """Генерирует случайное, но правдоподобное сообщение для коммита."""
    
    # Случайные действия
    actions = [
        "Обновление", "Добавление", "Рефакторинг", "Настройка", "Корректировка",
        "Интеграция", "Исправление", "Правка", "Внедрение"
    ]
    # Случайные объекты изменений, привязанные к кэшу или логам
    subjects = [
        f"временного кэша",
        f"системного лога",
        f"резервных копий данных",
        f"автоматических отчетов"
    ]
    
    # Добавим количество строк и номер итерации для отслеживания
    lines_info = f" (+{num_lines} lines)"
    iteration_info = f" [Commit {iteration}/{NUM_COMMITS}]"
    
    action = random.choice(actions)
    subject = random.choice(subjects)
    
    return f"{action}: {subject}{lines_info}{iteration_info}"

def run_git_command(command: list):
    """Выполняет команду Git и проверяет результат."""
    try:
        # Убедитесь, что команда выполняется в текущей директории
        result = subprocess.run(
            command, 
            check=True, 
            capture_output=True, 
            text=True,
            encoding='utf-8'
        )
        print(f"Успех: {' '.join(command)}")
        # print("Output:", result.stdout.strip())
        return True
    except subprocess.CalledProcessError as e:
        print(f"ОШИБКА выполнения команды Git: {' '.join(command)}")
        print("Stderr:", e.stderr.strip())
        print("Stdout:", e.stdout.strip())
        return False
    except FileNotFoundError:
        print("ОШИБКА: Git не найден. Убедитесь, что Git установлен и доступен в PATH.")
        return False

# --- ОСНОВНАЯ ЛОГИКА ---

def perform_activity_and_push():
    """
    Основная функция: генерирует контент, создает коммит и отправляет его в GitHub в цикле.
    """
    
    # 1. Проверяем, являемся ли мы репозиторием Git
    if not os.path.isdir(".git"):
        print("ОШИБКА: Похоже, вы находитесь не в директории репозитория Git.")
        print("Пожалуйста, клонируйте ваш репозиторий и запустите скрипт внутри него.")
        return

    # Запускаем цикл для выполнения нужного количества коммитов
    for i in range(1, NUM_COMMITS + 1):
        print(f"\n--- НАЧАЛО ИТЕРАЦИИ {i} из {NUM_COMMITS} (Генерация 500k строк) ---")
        
        # 2. Генерируем контент
        large_content = generate_large_content(NUM_LINES_TO_GENERATE)
        
        # 3. Записываем контент в файл
        filename_full_path = get_unique_filename()
        try:
            with open(filename_full_path, 'w', encoding='utf-8') as f:
                f.write(large_content)
            print(f"Файл '{filename_full_path}' создан с ~{len(large_content) / (1024*1024):.2f} MB данных.")
        except IOError as e:
            print(f"ОШИБКА при записи файла: {e}")
            continue # Переходим к следующей итерации

        # 4. Git Add (Добавляем содержимое папки 'cache' в индекс)
        if not run_git_command(["git", "add", CACHE_DIR]):
            continue 

        # 5. Git Commit (Фиксируем изменения)
        commit_message = generate_random_commit_message(filename_full_path, NUM_LINES_TO_GENERATE, i)
        print(f"-> Сообщение коммита: {commit_message}")
        if not run_git_command(["git", "commit", "-m", commit_message]):
            # Если коммит не удался, просто пропускаем push
            continue 

        # 6. Git Push (Отправляем в удаленный репозиторий)
        print("\n--- НАЧИНАЕТСЯ PUSH. Может занять время из-за объема данных. ---")
        # Предполагаем, что основная ветка называется 'main'. Если у вас 'master', замените.
        if run_git_command(["git", "push", "origin", "main"]): 
            print(f"--- УСПЕХ! Коммит {i}/{NUM_COMMITS} отправлен. ---")
        else:
            print(f"--- ОШИБКА PUSH для коммита {i}/{NUM_COMMITS}. Проверьте токен. ---")
        
        # 7. Задержка перед следующим пушем
        if i < NUM_COMMITS:
            delay_seconds = random.randint(10, 20) # Случайная задержка
            print(f"\nПауза {delay_seconds} секунд перед следующим коммитом...")
            time.sleep(delay_seconds)

    print("\n\n#####################################################################")
    print(f"ЗАВЕРШЕНО: Все {NUM_COMMITS} коммитов сгенерированы и отправлены.")
    print("#####################################################################")


if __name__ == '__main__':
    perform_activity_and_push()

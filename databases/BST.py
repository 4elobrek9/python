import random
import time


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def print_tree(root, level=0, prefix=""):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "|-- ")
            else:
                print(" " * ((level + 1) * 4) + "|-- None")
            if root.right:
                print_tree(root.right, level + 1, "|-- ")
            else:
                print(" " * ((level + 1) * 4) + "|-- None")


def interactive_search(root, key):
    steps = []
    start_time = time.time()
    current = root
    while current is not None:
        steps.append(f"Текущая нода: {current.val}")
        if key == current.val:
            steps.append(f"🎉 Найдено {key}!")
            break
        elif key < current.val:
            steps.append(f"{key} < {current.val} → идём влево")
            current = current.left
        else:
            steps.append(f"{key} > {current.val} → идём вправо")
            current = current.right
    end_time = time.time()
    return steps, end_time - start_time


# Генерация случайного дерева
random.seed(42)
values = random.sample(range(1, 50), 10)  # 10 чисел от 1 до 50
root = None
for v in values:
    root = insert(root, v)

# Вывод дерева
print("🌳 Дерево:")
print_tree(root)

# Ввод пользователя
try:
    target = int(input("\n🔍 Введите число для поиска: "))
except ValueError:
    print("Ошибка: введите целое число!")
    exit()

# Поиск с выводом шагов
print("\n🔎 Процесс поиска:")
steps, time_taken = interactive_search(root, target)
print("\n".join(steps))
print(f"\n⏱ Время поиска: {time_taken:.6f} сек.")

# Проверка, если число не найдено
if f"Найдено {target}!" not in "\n".join(steps):
    print(f"❌ Число {target} отсутствует в дереве.")
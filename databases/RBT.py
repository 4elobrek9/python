import random
import time

# Цвета нод
RED = "RED"
BLACK = "BLACK"


class RBNode:
    def __init__(self, key, color=RED):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, BLACK)  # Листья
        self.root = self.NIL

    def insert(self, key):
        new_node = RBNode(key)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._left_rotate(node.parent.parent)
        self.root.color = BLACK

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, key):
        steps = []
        start_time = time.time()
        current = self.root
        while current != self.NIL:
            steps.append(f"Нода: {current.key} ({current.color})")
            if key == current.key:
                steps.append(f"🎉 Найдено {key}!")
                break
            elif key < current.key:
                steps.append(f"{key} < {current.key} → идём влево")
                current = current.left
            else:
                steps.append(f"{key} > {current.key} → идём вправо")
                current = current.right
        end_time = time.time()
        return steps, end_time - start_time


def print_rb_tree(node, level=0, prefix=""):
    if node.key is not None:
        color = "🔴" if node.color == RED else "⚫"
        print(" " * (level * 4) + prefix + f"{node.key} {color}")
        if node.left.key is not None or node.right.key is not None:
            if node.left.key is not None:
                print_rb_tree(node.left, level + 1, "|-- ")
            else:
                print(" " * ((level + 1) * 4) + "|-- NIL")
            if node.right.key is not None:
                print_rb_tree(node.right, level + 1, "|-- ")
            else:
                print(" " * ((level + 1) * 4) + "|-- NIL")


# Генерация случайного дерева
random.seed(42)
values = random.sample(range(1, 100), 15)
rbt = RedBlackTree()
for v in values:
    rbt.insert(v)

# Вывод дерева
print("🌳 Красно-чёрное дерево:")
print_rb_tree(rbt.root)

# Интерактивный поиск
try:
    target = int(input("\n🔍 Введите число для поиска: "))
except ValueError:
    print("Ошибка: введите целое число!")
    exit()

print("\n🔎 Процесс поиска:")
steps, time_taken = rbt.search(target)
print("\n".join(steps))
print(f"\n⏱ Время поиска: {time_taken:.6f} сек.")

if f"Найдено {target}!" not in "\n".join(steps):
    print(f"❌ Число {target} отсутствует в дереве.")

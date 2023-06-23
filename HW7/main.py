from collections import deque 



class Stack():
    def __init__(self):
        self.my_stack = deque()

    def isEmpty(self):   # проверка стека на пустоту. Метод возвращает True или False.
        return len(self.my_stack) == 0

    def push(self, item):   # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.my_stack.append(item)

    def pop(self):   # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        return self.my_stack.pop()

    def peek(self):   # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        return self.my_stack[-1]

    def size(self):   # возвращает количество элементов в стеке.
        return len(self.my_stack)

def check(res):
    spis = {
            '(': ')',
            '[': ']',
            '{': '}'
    }
    for r in res:
        if r in spis.keys():
            stack.push(r)
        elif r in spis.values():
            if stack.isEmpty() or spis[stack.peek()] != r:
                return print("Несбалансированно.")
            stack.pop()
    if stack.isEmpty() == True:
        return print("Cбалансированно.")


if __name__ == "__main__":
    stack = Stack()
    proverka = [
            '(((([{}]))))',
            '[([])((([[[]]])))]{()}',
            '{{[()]}}',
            '}{}',
            '{{[(])]}}',
            '[[{())}]'
                ]

    for res in proverka:
        print(check(res))
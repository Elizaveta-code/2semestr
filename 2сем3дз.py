class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost
# Беллман-Форд
def can_get_rich(edges):
    # инициализируем все валюты бесконечностями
    currencies = {} # словарь для максимальных значений
    for edge in edges:
        currencies[edge.start] = float('-inf')
        currencies[edge.end] = float('-inf')
    currencies['RUB'] = 1
    for _ in range(len(currencies) - 1):
        for edge in edges:
            if currencies[edge.start] * edge.cost > currencies[edge.end]:
                currencies[edge.end] = currencies[edge.start] * edge.cost
    # проверка на положительный цикл
    for edge in edges:
        if currencies[edge.start] * edge.cost > currencies[edge.end]:
            return True  # нашли + цикл
    return False  # не нашли + цикл
# пример
edges = [
    Edge('RUB', 'USD', 2),  # 1 руб = 2 дол
    Edge('USD', 'EUR', 3),  # 1 дол = 3 евро
    Edge('EUR', 'RUB', 5)  # 1 евро = 5 руб
]
if can_get_rich(edges):
    print("Бесконечно обогатиться можно")
else:
    print("Бесконечно обогатиться нельзя")

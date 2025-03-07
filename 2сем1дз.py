class Graph:
    def __init__(self):
        self.graph = {}
        self.edges = {}  # словарь, который хранит ребра
# ключ словаря - кортеж (u, v) (или (v, u)), а значение = 1
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
        # записываем рёбра
        if (u, v) not in self.edges:
            self.edges[(u, v)] = 1
        if (v, u) not in self.edges:
            self.edges[(v, u)] = 1

    def find_start(self):
        nechet = [vertex for vertex in self.graph if len(self.graph[vertex]) % 2 == 1]
        if len(nechet) > 2:
            return "Эйлеров путь не существует"
        if len(nechet) == 0:  # граф замкнутый (но мб и изолированные вершины, на них пофиг)
            start_vertex = list(self.graph.keys())[0] # возьмем первую вершину, но это не принципиально
        else:
            start_vertex = nechet[0]  # начинаем с первой нечетной вершины
        return start_vertex

    def dfs(self, vertex, path):
        for neighbor in list(self.graph[vertex]):  # соседей vertex превращаем в список и итерируемся по ним
            if self.edges[(vertex, neighbor)] > 0:  # проверяем наличие ребра
                # удаляем ребро из графа
                self.edges[(vertex, neighbor)] -= 1
                self.edges[(neighbor, vertex)] -= 1
                path.append(neighbor)
                self.dfs(neighbor, path)  # рекурсивный вызов для соседа

    def euler_path(self):
        start_vertex = self.find_start()
        path = [start_vertex] # сначала в список просто первую вершину положили
        self.dfs(start_vertex, path)
        # проверяем, все ли рёбра использованы
        for count in self.edges.values():
            if count > 0:
                return "Эйлеров путь не существует"
        return path


# Пример:
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 3)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
'''g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)'''

'''g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(3, 6)
g.add_edge(4, 6)'''

euler_path = g.euler_path()
print("Эйлеров путь:", euler_path)

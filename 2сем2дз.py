# Алгоритм Джонсона = объединение Форда-Беллмана и Дейкстры
import heapq
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w)) # добавляем ключу-вершинке u значение-кортеж: соседа v (в которого шуруем от u), вес направленного ребра w
        if v not in self.graph:
            self.graph[v] = []

    def bellman_ford(self, start):
        distances = {vertex: float('inf') for vertex in self.graph} # словарь расстояний: ключ-номер вершинки, значения-бесконечности
        distances[start] = 0
        # рассматриваем все рёбра V-1 раз
        for _ in range(len(self.graph) - 1):
            for u in self.graph:
                for v, w in self.graph[u]:
                    if distances[u] != float('inf') and distances[u] + w < distances[v]:
                        distances[v] = distances[u] + w
        # проверка на наличие отрицательных циклов
        for u in self.graph:
            for v, w in self.graph[u]:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    return "Граф содержит отрицательный цикл"
        return distances

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            cur_dist, cur_node = heapq.heappop(priority_queue)
            if cur_dist > distances[cur_node]:
                continue
            for neighbor, weight in self.graph[cur_node]:
                distance = cur_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

    def johnson(self):
        f_graph = Graph() # делаем вспомогательный граф
        # добавляем все рёбра из оригинального графа в вспомогательный граф
        for u in self.graph:
            for v, w in self.graph[u]:
                f_graph.add_edge(u, v, w)
        # добавляем вспомогательную вершину с рёбрами ко всем другим вершинам
        for u in self.graph:
            f_graph.add_edge('f', u, 0)  # соединяем вспомогательную вершину со всеми другими
        # Беллман-Форд для нахождения расстояний от вспомогательной вершины
        f_distances = f_graph.bellman_ford('f')
        # пересчитываем веса рёбер
        new_graph = Graph()
        for u in self.graph:
            for v, w in self.graph[u]:
                new_weight = w + f_distances[u] - f_distances[v]
                new_graph.add_edge(u, v, new_weight)
        # Дейкстра для каждой вершины
        all_distances = {}
        for vertex in new_graph.graph: # тк new_graph - объект класса Graph, то к нему можно применить атрибут этого класса  и он будет считаться словарем
            all_distances[vertex] = new_graph.dijkstra(vertex)
        # возвращаем расстояния в исходные веса
        for u in all_distances:
            for v in all_distances[u]:
                all_distances[u][v] += f_distances[v] - f_distances[u]
        return all_distances
# пример
g = Graph()
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, -2)
g.add_edge(1, 3, 6)
g.add_edge(2, 3, 2)
all_distances = g.johnson()
print("Кратчайшие расстояния между всеми парами вершин:")
for u in all_distances:
    for v in all_distances[u]:
        print(f"От {u} до {v}: {all_distances[u][v]}")


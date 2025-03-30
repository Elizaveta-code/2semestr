'''
1) Обнуляют все потоки. Остаточная сеть изначально совпадает с исходной сетью.
2) В остаточной сети находят кратчайший путь из источника в сток. Если такого пути нет, останавливаются.
3) Пускают через найденный путь (увеличивающий путь или увеличивающая цепь) макс возможный поток - ребро с мин пропускной способностью.
4) Для каждого ребра на найденном пути увеличивают поток на мин пропускную способность, а в противоположном ему — уменьшают на неё же.
5) Если пропускная способность обнулилась, стирают ребро.
6) Возвращаются на шаг 2
'''
from collections import deque
M = int(input())  # Количество рёбер в графе
G = {}  # словарь словарей (список смежности), ключи — вершины графа, значения — словари смежных вершин с весами рёбер
for i in range(M):
    v1, v2, c = map(int, input().split())  # Ввод ребра: v1 -> v2 с пропускной способностью c
    if v1 not in G:
        G[v1] = {}  # создаём запись для вершины v1, если её ещё нет
    G[v1][v2] = c  # добавляем ребро v1 -> v2 с весом c
    if v2 not in G:
        G[v2] = {}
    G[v2][v1] = 0  # Обратное ребро с нулевой пропускной способностью
s = int(input())
f = int(input())
# Ищем кратчайший по числу ребер путь
def bfs(start, end):
    queue = deque([start])
    parents = {start: None}
    while queue:
        current = queue.popleft()
        for v in G[current]:
            if v not in parents and G[current][v] > 0:  # если вершина не посещена и есть остаточный поток
                parents[v] = current 
                if v == end:  # если достигли конечной вершины
                    return parents  # возвращаем путь
                queue.append(v)
    return None  # если путь не найден
def edmonds_karp(G, s, f):
    total_flow = 0
    while True:
        parents = bfs(s, f)
        if not parents:  # если путь не найден, выходим из цикла
            break
        flow = float('Inf')
        v = f
        while v != s:
            flow = min(flow, G[parents[v]][v])
            v = parents[v]
        v = f
        while v != s:
            u = parents[v]
            G[u][v] -= flow  # Уменьшаем пропускную способность прямого ребра
            G[v][u] += flow  # Увеличиваем пропускную способность обратного ребра
            v = parents[v]
        total_flow += flow
    return flow
print(edmonds_karp(G, s, f))

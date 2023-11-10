# from collections import deque, defaultdict
#
#
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         links = defaultdict(list)
#         if source == destination:
#             return True
#         for v1, v2 in edges:
#             links[v1].append(v2)
#             links[v2].append(v1)
#
#         search_queue = deque()
#         search_queue += links[source]
#         if destination in search_queue:
#             return True
#         searched = []
#         while search_queue:
#             if destination in search_queue:
#                 return True
#             vertice = search_queue.popleft()
#             if not vertice in searched:
#                 search_queue += links[vertice]
#                 searched.append(vertice)
#         return False

from collections import deque, defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        links = defaultdict(list)
        if source == destination:
            return True
        for v1, v2 in edges:
            links[v1].append(v2)
            links[v2].append(v1)

        search_queue = deque()
        search_queue += links[source]
        if destination in search_queue:
            return True
        searched = []
        while search_queue:
            if destination in search_queue:
                return True
            vertice = search_queue.popleft()
            if not vertice in searched:
                search_queue += links[vertice]
                searched.append(vertice)
        return False

from operator import itemgetter


class DisjointSet(dict):
    def add(self, item):
        self[item] = item

    def find(self, item):
        parent = self[item]

        while self[parent] != parent:
            parent = self[parent]

        self[item] = parent
        return parent

    def union(self, item1, item2):
        self[item2] = self[item1]


def kruskal(nodes, edges):
    forest = DisjointSet()
    mst = []
    for n in nodes:
        forest.add(n)

    sz = len(nodes) - 1

    for e in sorted(edges, key=itemgetter(2)):
        n1, n2, _ = e
        t1 = forest.find(n1)
        t2 = forest.find(n2)
        if t1 != t2:
            mst.append(e)
            sz -= 1
            if sz == 0:
                return mst

            forest.union(t1, t2)


# test

nodes = list("123456")
edges = [("1", "2", 1), ("1", "4", 2),
         ("2", "4", 4), ("2", "3", 6), ("2", "5", 7),
         ("3", "6", 5),
         ("5", "6", 4), ("4", "5", 9), ["3", "5", 8]]

print(kruskal(nodes, edges))
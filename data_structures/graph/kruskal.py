

class Edge:
    def __init__(self, from_, to_, weight):
        self.f = from_
        self.t = to_
        self.w = weight

    def __str__(self):
        return f"{self.f} <==> {self.t} | {self.w}"

    def dump(self):
        return self.f, self.t, self.w

class Graph:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.mst = None

    def add(self, edge):
        self.edges.append(edge)

    def get_accessible_edges(self, vertex, lookup):
        prev = set()
        curr = set([vertex])

        while prev != curr:
            prev = prev.union(curr)

            for edge in lookup:
                f, t, _ = edge.dump()

                if f in prev and t in prev:
                    continue

                elif f in prev:
                    curr.add(t)
                
                elif t in prev:
                    curr.add(f)

        return curr

    def kruskal(self):
        mst = []
        edges = sorted(self.edges, key = lambda x: x.w)
        
        for edge in edges:
            f, t, _ = edge.dump()

            if mst == []:
                mst.append(edge)

            else:
                f_accessible = set(self.get_accessible_edges(f, mst))
                t_accessible = set(self.get_accessible_edges(t, mst))

                if len(f_accessible.intersection(t_accessible)) == 0:
                    mst.append(edge)

        self.mst = mst

    def dump(self):
        print(self.name)
        self.mst.sort(key = lambda x: x.f)

        if self.mst:
            for edge in self.mst:
                print(edge)

        else:
            print("[NO MINIMUM SPANNING CALCULATED")

        print()


# ------------------ [GEEKS FOR GEEKS] ------------------ #

gfg = Graph("Greeks for greeks")

gfg.add(Edge(0, 1, 4))
gfg.add(Edge(1, 2, 8))
gfg.add(Edge(2, 3, 7))
gfg.add(Edge(3, 4, 9))
gfg.add(Edge(4, 5, 10))
gfg.add(Edge(5, 6, 2))
gfg.add(Edge(6, 7, 1))
gfg.add(Edge(0, 7, 8))

gfg.add(Edge(1, 7, 11))
gfg.add(Edge(2, 8, 2))
gfg.add(Edge(6, 8, 6))
gfg.add(Edge(7, 8, 7))
gfg.add(Edge(2, 5, 4))
gfg.add(Edge(3, 5, 14))

gfg.kruskal()
gfg.dump()

# --------------------- [JAVATPOINT] -------------------- #

java = Graph("Java")

java.add(Edge('a', 'b', 1))
java.add(Edge('b', 'c', 3))
java.add(Edge('c', 'd', 4))
java.add(Edge('d', 'e', 2))
java.add(Edge('a', 'e', 5))

java.add(Edge('a', 'c', 7))
java.add(Edge('a', 'd', 10))

java.kruskal()
java.dump()

# ------------------- [GATEVIDHYALA] ------------------- #

gate = Graph("Gate")

gate.add(Edge(1, 2, 28))
gate.add(Edge(2, 3, 16))
gate.add(Edge(3, 4, 12))
gate.add(Edge(4, 5, 22))
gate.add(Edge(5, 6, 25))
gate.add(Edge(1, 6, 10))

gate.add(Edge(2, 7, 14))
gate.add(Edge(4, 7, 18))
gate.add(Edge(5, 7, 24))

gate.kruskal()
gate.dump()

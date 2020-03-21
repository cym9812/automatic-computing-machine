seen = [0, 9, 1, 5, 4, 3, 2]
done = [13, 10, 12, 6, 7, 8, 11]
class Arc:
    def __init__(self, seen, done):
        self.seen = seen
        self.done = done
arcs = {}
for i in range(0, 7):
    arcs[i + 1] = Arc(seen[i], done[i])

for key in arcs.keys():
    for another_key in arcs.keys():
        if key != another_key:
            a = arcs[key]
            b = arcs[another_key]
            if a.seen < b.seen < b.done < a.done:
                print("({0}, {1}) is tree".format(key, another_key))
            elif b.seen < a.seen < a.done < b.done:
                print("({0}, {1}) is back".format(key, another_key))
            elif b.seen < b.done < a.seen < a.done:
                print("({0}, {1}) is cross".format(key, another_key))
            else:print("({0}, {1}) is nothing".format(key, another_key))
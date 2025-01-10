def destinCity(paths):
    map = {}
    for path in paths:
        map[path[0]] = path[1]

    for m in map.values():
        if m not in map.keys():
            return m



print(destinCity([["B","C"],["D","B"],["C","A"]]))
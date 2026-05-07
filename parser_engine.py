def parse(start, target, cfg):
    from collections import deque
    queue = deque()
    # queue.append((start, [start]))
    queue.append((start, [start], []))

    visited = set()

    while queue:

        current, path, history = queue.popleft()
        # current, path = queue.popleft()

        if current == target:
            # return True, path
            return True, path, history

        if len(current) > len(target) + 2:
            continue

        # avoid loops
        if current in visited:
            continue

        visited.add(current)

        for i in range(len(current)):
            symbol = current[i]

            if symbol in cfg:
                for production in cfg[symbol]:

                    new_string = current[:i] + production + current[i+1:]

                    new_history = history + [(symbol, production, i)]

                    queue.append((new_string, path + [new_string], new_history))
                    # queue.append((new_string, path + [new_string]))

    # return False, []
    return False, [], []
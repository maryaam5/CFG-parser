def parse(start, target, cfg):
    from collections import deque

    queue = deque()
    queue.append((start, [start]))

    visited = set()

    while queue:

        current, path = queue.popleft()

        if current == target:
            return True, path

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

                    queue.append((new_string, path + [new_string]))

    return False, []
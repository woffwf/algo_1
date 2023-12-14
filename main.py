from collections import defaultdict, deque


def find_minimum_depth(adj_list, start_node):
    visited = set()
    depth = 0
    queue = deque([(start_node, depth)])

    while queue:
        node, depth = queue.popleft()
        visited.add(node)

        is_leaf = True
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))
                is_leaf = False

        if is_leaf:
            return depth + 1


def main():

    adj_list = defaultdict(list)
    with open('input.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) == 2:
                u, v = map(int, data)
                adj_list[u].append(v)
                adj_list[v].append(u)


    root = 1


    min_depth = find_minimum_depth(adj_list, root)


    with open('output.txt', 'w') as file:
        file.write(str(min_depth))


if __name__ == "__main__":
    main()

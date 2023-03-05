# python3
#Keita Matvijuka 13. grupa Apl. nr. 221RDB506


import sys
import threading


def compute_height(num_nodes, parent_indices):
    nodes = [[] for _ in range(num_nodes)]
    root = None
    for i, parent_index in enumerate(parent_indices):
        if parent_index == -1:
            root = i
        else:
            nodes[parent_index].append(i)
    max_height = calculate_max_node_height(nodes, root)
    return max_height


def calculate_max_node_height(nodes, root):
    stack = [(root, 1)]
    max_height = 1
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        for child in nodes[node]:
            stack.append((child, height + 1))
    return max_height


def main():
    user_input = input()
    if "a" not in user_input:
        if "I" in user_input:
            num_nodes = int(input())
            parent_indices = list(map(int, input().split()))
            max_height = compute_height(num_nodes, parent_indices)
            print(max_height)
        elif "F" in user_input:
            file_path = "test/" + input()
            with open(file_path, 'r') as f:
                num_nodes = int(f.readline().strip())
                parent_indices = list(map(int, f.readline().strip().split()))
                max_height = compute_height(num_nodes, parent_indices)
                print(max_height)


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

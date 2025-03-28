import sys

tree = {}


def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])


def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')


def sol():
    read = sys.stdin.read().splitlines()
    n = int(read[0])
    for i in range(1, n + 1):
        root, left, right = read[i].split()
        tree[root] = [left, right]

    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')


sol()

lst = [9, 4, 12, 3, 6, 15, 13, 17]
TREE = [0] * 100
N = 100

def insert(value):
    root = 1
    while root<N and TREE[root]:
        if TREE[root] < value:
            root = root*2+1
        else:
            root = root*2
    TREE[root] = value


def find(key):
    root = 1
    while TREE[root]:
        if TREE[root] == key:
            return root
        if TREE[root] < key:
            root = root*2 + 1
        else:
            root = root*2
    return -1

for data in lst:
    insert(data)
    print(TREE)

insert(5)
print(TREE)

print(find(5))
print(find(3))
print(find(9))
print(find(17))
print(find(50))
print(find(1))

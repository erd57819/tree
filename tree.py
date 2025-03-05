N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

TREE = [[] for _ in range(N+1)]
lst = list(map(int, s.split()))
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    TREE[p].append(c)

print(TREE)

def pre_order(root):
    print(root)
    if len(TREE[root]) > 0: #왼쪽트리가 있으면:
        pre_order(TREE[root][0])
    if len(TREE[root]) > 1:
        pre_order(TREE[root][1])

pre_order(1)

print('==========')
def in_order(root):
    if len(TREE[root]) > 0: #왼쪽트리가 있으면:
        in_order(TREE[root][0])
    print(root)
    if len(TREE[root]) > 1:
        in_order(TREE[root][1])

in_order(1)
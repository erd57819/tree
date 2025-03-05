N = 10
TREE = [0] * (N+1)
for i in range(10):
    TREE[i+1] = chr(ord('A') + i)
print(TREE)

pre_order(1)
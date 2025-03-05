n=13
s= '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

# 방향성이 없을 경우
tree = [[] for _ in range(n+1)]
lst = list(map(int,s.split()))
for i in range(0,len(lst),2):
    p=lst[i]
    c=lst[i+1]
    tree[p].append(c)
print(tree)

def pre_order(root):
    print(root)
    if len(tree[root])>0: # 왼쪽 트리가 있으면 
        pre_order(tree[root][0])
    if len(tree[root])>1: # 오른쪽 트리가 있으면
        pre_order(tree[root][1])
pre_order(1)

print('+++++++++++++++++++++++++++')

def in_order(root):
    if len(tree[root])>0: # 왼쪽 트리가 있으면 
        in_order(tree[root][0])
    print(root)
    if len(tree[root])>1: # 오른쪽 트리가 있으면
        in_order(tree[root][1])
in_order(1)


print('===========================')


# 방향성이 있을 경우
tree = [[0,0]for _ in range(n+1)]
lst = list(map(int,s.split()))
for i in range(0,len(lst),2):
    p=lst[i]
    c=lst[i+1]
    if tree[p][0]: #왼족에 데이터가 있으면 
        tree[p][1] = c
    else:
        tree[p][0] =c
print(tree)


def pre_order(root):
    print(root)
    if tree[root][0]: # 왼쪽 트리가 있으면 
        pre_order(tree[root][0])
    if tree[root][1]: # 오른쪽 트리가 있으면
        pre_order(tree[root][1])
pre_order(1)


def pre_order(t):
    if t:
        print(t)
        pre_order(tree[t][0])
        pre_order(tree[t][1])


print('+++++++++++++++++++++++++++')


def in_order(root):
    if tree[root][0]>0: # 왼쪽 트리가 있으면 
        in_order(tree[root][0])
    print(root)
    if tree[root][1]: # 오른쪽 트리가 있으면
        in_order(tree[root][1])
in_order(1)

print('================================')


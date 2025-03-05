def insert(value):
    p = 1
    while tree[p]:
        if tree[p] < value:
            p = p+1
        else:
            p=p*2
    tree[p] = value
        

n = 8
lst=[9,4,12,3,6,15,13,17]
tree = [0]*100

for data in lst:
    insert(data)
    print(tree)
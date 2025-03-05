def inorder(t):
    global num
    if t <= N:  
        inorder(t * 2) 
        tree[t] = num  
        num += 1
        inorder(t * 2 + 1)  
T = int(input())  
for tc in range(1, T + 1):
    N = int(input())  
    tree = [0] * (N + 1)  
    num = 1  
    inorder(1)  
    root = tree[1]  
    half = tree[N // 2]  
    print(f"#{tc} {root} {half}")


    

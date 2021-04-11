# %%
def formule(x, y):
    out = 0
    if x >=2 and y >= 4:
        out += min(x, y//2) - 1
    if x >=4 and y >=2:
        out += min(y, x//2) - 1
    return out
    
def build_mat(board):
    n_row, n_col = len(board), len(board[0])
    
    B = [[0 for i in range(n_col)] for j in range(n_row)]
    H = [[0 for i in range(n_col)] for j in range(n_row)]
    R = [[0 for i in range(n_col)] for j in range(n_row)]
    L = [[0 for i in range(n_col)] for j in range(n_row)]
    
    B[0] = [x for x in board[0]]
    for i in range(1, n_row):
        for j in range(n_col):
            if board[i-1][j] != 0 and board[i][j] != 0:
                B[i][j] = B[i-1][j] 
            B[i][j] += board[i][j]
    
    H[n_row-1] = [x for x in board[n_row-1]]
    for i in range(n_row-2, -1, -1):
        for j in range(n_col):
            if board[i+1][j] != 0 and board[i][j]!= 0:
                H[i][j] = H[i+1][j]
            H[i][j] += board[i][j]
            
    for i in range(n_row):
        for j in range(n_col):
            if j >= 1 and board[i][j-1] != 0 and board[i][j]!= 0:
                R[i][j] = R[i][j-1]
            R[i][j] += board[i][j]
            
    for i in range(n_row):
        for j in range(n_col-1, -1, -1):
            if j <= n_col-2 and board[i][j+1] != 0 and board[i][j]!= 0:
                L[i][j] = L[i][j+1]
            L[i][j] += board[i][j]
    return B, H, R, L
    
#%%
T = int(input())

for t in range(T):
    n_row, n_col = [int(i) for i in input().split()]
    #print(n_row, n_col)
    board = []
    for r in range(n_row):
        board.append([int(i) for i in input().split()])
    
    #print(board)
    B, H, R, L = build_mat(board)
    # print("B: \n", B, "\n")
    # print("H: \n", H, "\n")
    # print("R: \n", R, "\n")
    # print("L: \n", L, "\n")
    ans = 0
    for i in range(n_row):
        for j in range(n_col):
            # normal L 
            d = ans
            ans += formule(L[i][j], B[i][j])
            
            # mirror L
            ans += formule(R[i][j], B[i][j])
            
            # upside down L
            ans += formule(L[i][j], H[i][j])
            
            # upside down mirror L
            ans += formule(H[i][j], R[i][j])
           # if ans-d != 0:
            #    print(f"({i},{j}): n_L = {ans-d}")
    print("Case #{}: {}".format(t+1, ans))
# %%

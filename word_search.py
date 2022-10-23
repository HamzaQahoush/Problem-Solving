def word_search(board,word):
    R=len(board)
    C=len(board[0])
    visited=set()
    def dfs(i,j,idx):
        if idx==len(word): return True
        if i >=R or j >=C or i <0 or j <0 or word[idx] != board[i][j] or (i,j) in visited:
            return False
        visited.add((i,j))
        res=(dfs(i+1,j,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i,j-1,idx+1))
        visited.remove((i,j))
        
        return res
    
    for i in range (R) :
        for j in range (C):
            if dfs(i,j,0) : return True
    return False
    
    


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(word_search(board,word))
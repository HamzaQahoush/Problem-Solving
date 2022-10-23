
def spiralOrder( matrix) :
  T= 0
  B= len(matrix)-1
  R=len(matrix[0])-1
  L= 0
  res=[]
  dir_=0
  while T <= B and  L<=R :
      if dir_==0 :
          for i in range(L,R+1):
              res.append(matrix[T][i])
          T+=1
      elif dir_==1:
          for i in range(T,B+1):
              res.append(matrix[i][R])
          R -=1
      elif dir_==2 :
          for i in range(R,L-1,-1):
              res.append(matrix[B][i])  
          B-=1
          
      elif dir_==3:
          for i in range(B,T-1,-1):
              res.append(matrix[i][L])
          L+=1
     
      dir_=(1 + dir_)%4
  return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))
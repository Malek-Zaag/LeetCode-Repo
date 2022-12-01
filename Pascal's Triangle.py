import sys 


sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")
t=int(input())

def main():
  for k in range(t):
    numRows=int(input())
    if numRows==0: print([])
    if numRows==1: print([[1]])
    res=[[1]]
    c=1
    for i in range(1,numRows):
      c+=1
      b=[]
      b.append(1)
      b.insert(c-1,1)
      for j in range(1,c-1):
        b.insert(j,res[i-1][j-1]+ res[i-1][j])
      res.append(b)
    print(res)
main()
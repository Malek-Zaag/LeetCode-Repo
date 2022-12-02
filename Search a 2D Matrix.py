import sys


sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")

t=int(input())


def main():
  for i in range(t):
    matrix=list(map(int,input().split()))
    matrix=[matrix[:4],matrix[4:8],matrix[8:12],matrix[12:16]]
    target=int(input())
    found=False
    for j in range(len(matrix)):
      if target in matrix[j]: found=True
    print(found)
    
    
main()
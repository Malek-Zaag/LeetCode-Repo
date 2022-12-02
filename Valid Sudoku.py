import collections
import sys



sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")

t=int(input())

def main():
  for i in range(t):
    board=list(map(int,input().split()))
    board=[board[:3],board[3:6],board[6:9]]
    print(board)
    valid=True
    # check row
    for row in board:
      space1=[i for i in row if i!="."]
      valid=len(set(space1))== len(space1)
    #check column
    for col in zip(*board):
      space2=[i for i in col if i!="."]
      valid=len(set(space2))== len(space2)
    for i in range(0,3,6):
      for j in range(0,3,6):
        mat=[board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
        for z in mat:
          space3=[i for i in z if i!="."]
          valid3=len(set(space3))==len(space3)
        for z in zip(*mat):
          space4=[i for i in z if i!="."]
          valid4=len(set(space4))==len(space4)
    print(valid)
main()
from ctypes import memset
from itertools import count
import sys
import numpy as np


sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")


t=int(input())


def main():
  for k in range(t):
    mat=list(map(int,input().split()))
    r,c=map(int,input().split())
    mat=[mat[:2],mat[2:]]
    n,m=len(mat),len(mat[0])
    if (n*m!= r*c): print(mat)
    res=[[0 for y in range(c)] for j in range(r)]
    for i in range(r*c):
      res[i//c][i%c]=mat[i//m][i%m]
    print(res)
main()
  
  
  
                
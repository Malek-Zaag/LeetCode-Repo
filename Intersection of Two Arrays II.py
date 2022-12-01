import collections
import sys

sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")


t=int(input())


def main():
  for y in range(0,t):
    nums1=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    a, b = map(collections.Counter, (nums1, nums2))
    print(list((a & b).elements()))
        
       
  
  
main()
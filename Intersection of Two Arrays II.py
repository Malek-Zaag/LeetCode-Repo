import sys

sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")


t=int(input())


def main():
  for y in range(0,t):
    nums1=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    res=[]
    d={}
    if len(nums1) - len(nums2) > 0:
      for i,j in enumerate(nums2):
        if j in nums1 and d.get(i) == None:
          res.append(j)
        d[i]=j
    else:
      for i,j in enumerate(nums1):
        if j in nums2 and d.get(i) == None:
          res.append(j)
        d[i]=j
    print(res)
        
       
  
  
main()
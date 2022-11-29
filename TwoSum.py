import sys
sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")


t=int(input())



def helper():
  pass


def main():
  for j in range(0,t):
    nums= list(map(int,input().split()))
    target=nums[len(nums)-1]
    d={}
    for i,n in enumerate(nums):
      rem=target-n
      if n in d: 
        print(d[n],i)
      d[rem]= i 
      
main()
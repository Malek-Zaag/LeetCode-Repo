import sys
sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")


t=int(input())

def main():
  for i in range(t):
    nums=list(map(int,input().split()))
    ans=nums[0]
    curr=0
    for i in nums:
      if curr < 0:
        curr=0
      curr +=i
      ans=max(ans,curr)
    print(ans)

main()
import sys
sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")


t=int(input())



def helper():
  pass


def main():
  for i in range(0,t):
    nums= list(map(int,input().split()))
    target=nums[len(nums)-1]
    li=[]
    for i in range(0,len(nums)-1):
      for j in range(i+1,len(nums)):
        if nums[i]+ nums[j] == target:
          li=[i,j]
          print(i,j)
        else:
          continue
    print(li)
main()
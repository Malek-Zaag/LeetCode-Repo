import sys
sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")


t=int(input())



def main():
  for i in range(t):
    nums=list(map(int,input().split()))
    sett=set()
    for z in range(len(nums)):
      sett.add(nums[z])
    if len(nums)==len(sett):
      print("false")
    else:
      print("true")  
      
      
main()
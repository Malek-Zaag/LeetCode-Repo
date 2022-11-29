import sys

sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")


t=int(input())



def main():
  for i in range(0,t):
    nums1=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    m=nums1.pop()
    n=nums2.pop()
    nums1[:]=nums1[:m]
    nums2[:]=nums2[:n]
    nums1+=nums2
    nums1.sort()
    print(nums1)
main()
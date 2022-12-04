import collections
import sys

sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")

te=int(input())

def main():
  for i in range(te):
    s=input()
    t=input()
    a,b=map(collections.Counter,(s,t))
    if a ==b:
      print(True)
    else:
      print(False)

main()
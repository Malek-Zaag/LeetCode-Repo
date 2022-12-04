import collections
import sys



sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")

t=int(input())

def main():
  for i in range(t):
    ransomNote=input()
    magazine=input()
    a,b=map(collections.Counter,(ransomNote,magazine))
    result=True
    li=dict(b.items())
    for j in a.items(): 
      print(li)   
      if j[0] in li.keys() and j[1] <= li[j[0]]:
          result=True
      else:
        result=False
        break
    print(result)
main()
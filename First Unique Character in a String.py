import collections
import sys



sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")

t=int(input())

def main():
  for i in range(t):
    s=input()
    a=collections.Counter(s)
    print(a.items())
    char=-1
    for i in a.items():
      if i[1] == 1:
        print(i)
        char=s.index(i[0])
        break
    print(char)
main()
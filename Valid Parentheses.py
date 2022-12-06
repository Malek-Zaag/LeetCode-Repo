import sys


sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")

t=int(input())

def main():
  for i in range(t):
    s=input()
    d = {'(':')', '{':'}','[':']'}
    stack = []
    for i in s:
      if i in d:  # 1
        stack.append(i)
      elif len(stack) == 0 or d[stack.pop()] != i:  # 2
        return False
    return len(stack) == 0

main()
  
  
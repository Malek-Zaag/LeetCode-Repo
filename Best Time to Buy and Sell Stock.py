import sys
sys.stdin=open("./input.txt","r")
sys.stdout=open("./output.txt","w")


t=int(input())


def main(): 
  for i in range(0,t):
    prices=list(map(int,input().split()))
    max_profit, min_price = 0, float('inf')
    for price in prices:
      min_price = min(min_price, price)
      profit = price - min_price
      max_profit = max(max_profit, profit)
    print (max_profit)
main()
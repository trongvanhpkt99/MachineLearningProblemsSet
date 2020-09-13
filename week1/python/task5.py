if __name__ == '__main__':
  #n = int(input())
  # your code here
  ip=[2,1,3,5,6,9,7]
  ip=sorted(ip)
  x=ip[0]
  y=ip[0]
  for i in ip:
    if i >y:
      x=y
      y=i
  print(x)

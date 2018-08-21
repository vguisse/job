def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def max(a, b):
  if a > b:
    return a
  else:
    return b

print(max(fact(3), 12))

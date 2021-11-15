# In this code, we take inputs a and c.
# In b and d we take the set input values with space, then we convert them to sets and find the difference and sort them
a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
x=set(b)
y=set(d)
p=y.difference(x)
q=x.difference(y)
r=p.union(q)
print ('\n'.join(sorted(r, key=int)))

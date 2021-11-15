# Apply your knowledge of the .add() operation to help your friend Rupal.

# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.
# Find the total number of distinct country stamps.
# Input Format
# The first line contains an integer , the total number of country stamps.
# The next  lines contains the name of the country where the stamp is from.
# Constraints
# 0 < N < 1000
# Output Format
# Output the total number of distinct country stamps on a single line


N = int(input())
a = set()
for i in range(N):
    names = input()
    a.add(names)
print(len(a))



# You have a non-empty set , and you have to execute  commands given in  lines.
# The commands will be pop, remove and discard.
# for this we are storing the commands in dictionary and checking the condition

n = int(input())
s = set(map(int, input().split()))
d = {"pop":s.pop, "remove":s.remove, "discard": s.discard}
for _ in range(int(input())):
    c = input().split()
    d[c[0]](int(c[1])) if len(c)>1 else d[c[0]]()
print(sum(s))
    

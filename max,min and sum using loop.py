#to find the sum of the elements of a list
l=[10,12,34,54]
s=0
for i in range(0,len(l)):
    s+=l[i]
print(f"Sum of the elements in the list: {s}")
min=0
for i in range(0,len(l)):
    if l[i]<l[i-1]:
        min=l[i]
print(f"Minimum element in the list: {min}")
max=0
for i in range(0,len(l)):
    if l[i]>l[i-1]:
        max=l[i]
print(f"Maximum element in the list: {max}")
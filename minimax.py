def minimax(values,flag=True):
    new=[]
    for i in range(0,len(values)-1,2):
        if flag:
            new.append(max(values[i],values[i+1]))
        else:
            new.append(min(values[i],values[i+1]))
        if len(values)%2:
            new.append(values[-1])

    return minimax(new,not flag) if len(new)>1 else new[0]

leaf=[]
n=int(input("Enter n: "))
for i in range(0,n):
    li=int(input("Enter nos: "))
    leaf.append(li)

print("The root of the tree is ",minimax(leaf))
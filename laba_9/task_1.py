A = ['a', 'b', 'c', 'd', 'e']
for i in A:
    A.append(i*2)
    if i == 'd':
        break
print(A)
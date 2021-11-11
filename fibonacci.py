a,b = 0,1
print(b, end=' ')

for i in range(0,50):
    a,b = b,b+a
    if b <= 50:
        print(b,end=' ')
1 1 2 3 5 8 13 21 34
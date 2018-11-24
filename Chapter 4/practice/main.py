perline=10
for var in range(100):
    if (var+1<10):
        print(var+1, "  ", end='')
    else:
        print(var+1, " ",end='')
    if(var%10==perline-1):
        print('\n')
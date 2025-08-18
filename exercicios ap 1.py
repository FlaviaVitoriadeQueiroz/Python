def nfat(L):
    n = 0
    fat = 1
    while fat <= L:
        n += 1
        fat *=n
    return n-1
    print(n)
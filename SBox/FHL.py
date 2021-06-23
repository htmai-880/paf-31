def FHL(X):    
    h = 1
    longX = len(X)
    while h < longX:
        for i in range(0, longX, h * 2):
            for j in range(i, i + h):
                y = X[j]
                z = X[j + h]
                X[j] = y + z
                X[j + h] = y - z
        h *= 2
    return X

def prime(x):
    prime = []
    marked = []
    for i in range(2,x+1):
        if i not in marked:
            prime.append(i)
            for j in range(i*i, x+1, i):
                marked.append(j)
    return prime
prime(100)
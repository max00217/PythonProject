for i in range(5000000):
    if i == sum(int(x) ** int(x) for x in str(i)):
        print(i)
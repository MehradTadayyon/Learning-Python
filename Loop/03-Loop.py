for i in range(1,10):
    for j in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                num = i*1000 + j*100 + y*10 + z
                if z + i**4 == y**2 + j**3:
                    print(num)
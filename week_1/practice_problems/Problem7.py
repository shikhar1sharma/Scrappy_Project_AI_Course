def pattern2(num):
    for n in range(1, num+1):
        print(' ' * (num - n) + '*' * n)


pattern2(4)
d1 = {}
with open('assignment8.csv','r') as xy:
    for line in xy:
        y = line.strip().split(',')
        d1[y[0]]=y[1]
print(d1)
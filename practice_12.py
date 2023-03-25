h_dict = { }
f = open('ass.csv',"r")
for y in f:
    x=y.strip().split(',')
    h_dict[x[0]]=x[1]
print(h_dict)
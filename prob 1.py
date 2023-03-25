def power():
    # res = []
    # for x in h_list:
    #     h = x ** input_int
    #     res.append(h)
    res = [x ** input_int for x in h_list]
    print(res)


h_list = []
ele = list(input("enter the elements of the list : "))
for i in ele:
    h_list.append(int(i))
print(h_list)
input_int = int(input("enter the value to be powered : "))

power()

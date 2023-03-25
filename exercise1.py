def sortbylength(list1):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if len(list1[i]) < len(list1[j]):
                list1[i], list1[j] = list1[j], list1[i]

    return list1


print(sortbylength(["a", "ccc", "dddd", "bb"]))  # ["a", "bb", "ccc", "dddd"]

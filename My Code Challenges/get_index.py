indices = []
def index_all(lst,item):
    for i in range(len(lst)):
        if type(lst[i])==list and item in lst[i]:
            indices.append([0])
            index_all(lst[i], item)
        else:
            if lst[i] == 2:
                indices.append(i)
def unique_elements(mylist):
    return list(dict.fromkeys(mylist))


mylist = input().split()

unique_list = unique_elements(mylist)
print(" ".join(unique_list))
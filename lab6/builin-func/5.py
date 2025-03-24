def check_for_true(elements):
    if all(elements):
        print("All elements are true")
    else:
        print("All elements are not true")

elements = (1, "b", "a", 2, "V", -1)  
check_for_true(elements)

elements2 = (1, 0, "a", 2, "V", -1)  
check_for_true(elements2)


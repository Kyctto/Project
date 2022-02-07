def min_element(new_list):
    min_value = new_list[0]
    for elem in new_list:
        if elem < min_value:
            min_value = elem
    return min_value

def list_sorter(new_list):
    sorted_list = []
    while new_list:
        smillest = min_element(new_list=new_list)
        sorted_list.append(smillest)
        new_list.remove(smillest)
    return sorted_list


some_list = [-40, 0, 35, 15, 48, -40, 99, -5]

print(min_element(some_list))

print(list_sorter(some_list))
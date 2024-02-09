list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = ["a", "b", "c"]
list_d = ["d", "e", "f"]

def fusion_listes(list_one, list_two):
    merge_list = []
    for element in list_one:
        merge_list.append(element)
    for element in list_two:
        merge_list.append(element)
    print(merge_list)

merged_lists = fusion_listes(list_a, list_b)
merged_lists_two = fusion_listes(list_c, list_d)
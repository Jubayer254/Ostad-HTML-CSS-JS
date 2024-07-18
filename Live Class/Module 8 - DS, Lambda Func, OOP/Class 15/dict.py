# MERGE 2 DICTS

def merge_dicts(dict1, dict2):
    dict_result = {}
    dict_result.update(dict1)
    dict_result.update(dict2)
    return dict_result

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "d": 4}
print(merge_dicts(dict1, dict2))
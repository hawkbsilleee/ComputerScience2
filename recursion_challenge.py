# def get_permutation(string):

#     permutations = []
#     tuple_range = (len(string), 0)

#     for index in range(tuple_range):
#         permutation += string[index]

#     if permutation == string:
#         return permutations.append(permutation)
#     else:
#         return tuple_range[0]
import random

def get_permutation(string):

    def gen_string(string):
        new_string = {}
        for character in string:
            new_string.add(character)
        return new_string

    old_string = string
           
    permutations = []
    if len(string) == 1: 
        permutations.append(string)
        return permutations
    else: 
        new_string = gen_string(string)
        if old_string != new_string:
            return new_string.append(list)

    



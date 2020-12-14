import random

def read_names(names_file_name):
    with open(names_file_name, 'r') as names_file:
        names = names_file.readlines()
        for name_index in range(len(names)):
            names[name_index] = names[name_index].replace('\n', '')
    return names


def mix_names(names):
    pairs = []; taken = []
    for name_index in range(0, len(names)):
        pair = name_index
        while pair == name_index or pair in taken:
            pair = random.randint(0, len(names)-1)
        taken.append(pair)
        pairs.append((names[name_index], names[pair]))
    return pairs

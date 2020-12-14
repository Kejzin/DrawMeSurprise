def read_names():
    with open('names.txt', 'r') as names_file:
        names = names_file.readlines()
        for name_index in range(len(names)):
            names[name_index] = names[name_index].replace('\n', '')
    return names

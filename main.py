def read_names(names_file_name):
    with open(names_file_name, 'r') as names_file:
        names = names_file.readlines()
        for name_index in range(len(names)):
            names[name_index] = names[name_index].replace('\n', '')
    return names

